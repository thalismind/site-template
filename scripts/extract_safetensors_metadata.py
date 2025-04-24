import json
from pathlib import Path
from safetensors.torch import safe_open

def parse_optimizer(optimizer_str):
    """
    Parses the ss_optimizer string into structured metadata using string splitting.
    Example input:
    prodigyopt.prodigy.Prodigy(decouple=True,weight_decay=0.15,betas=(0.9, 0.999),use_bias_correction=False,safeguard_warmup=False,d_coef=2)
    """
    metadata = {
        "d_coef": 1.0,
        "weight_decay": None,
    }

    if not optimizer_str.endswith(")"):
        return metadata  # malformed input

    # Split off the arguments part
    head, _, tail = optimizer_str.partition("(")
    metadata["optimizer_name"] = head.split(".")[-1]

    # Remove the trailing ')'
    tail = tail[:-1]

    # Split by comma, but don't split inside parentheses (like in betas)
    args = []
    depth = 0
    current = ""
    for char in tail:
        if char == "," and depth == 0:
            args.append(current.strip())
            current = ""
        else:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            current += char
    if current:
        args.append(current.strip())

    # Process each key=value pair
    for pair in args:
        if "=" not in pair:
            continue
        key, _, value = pair.partition("=")
        key = key.strip()
        value = value.strip()
        print(f"Parsing {key} = {value}")

        if key == "weight_decay":
            metadata["weight_decay"] = float(value)
        elif key == "betas":
            try:
                metadata["betas"] = eval(value)
            except Exception:
                metadata["betas"] = value
        elif key == "d_coef":
            metadata["d_coef"] = float(value)

    return metadata

def parse_network_args(args_json):
    """
    Parses ss_network_args JSON string.
    """
    metadata = {}
    try:
        args = json.loads(args_json)
        if "algo" in args:
            metadata["algo"] = args["algo"]
        if "conv_dim" in args:
            try:
                metadata["conv_dim"] = int(args["conv_dim"])
            except ValueError:
                pass
        if "conv_alpha" in args:
            try:
                metadata["conv_alpha"] = int(args["conv_alpha"])
            except ValueError:
                pass
    except Exception as e:
        print(f"Failed to parse ss_network_args: {e}")
    return metadata


def readable_network_module(module_str):
    if module_str == "lycoris.kohya":
        return "lycoris"
    elif module_str == "networks.lora_flux":
        return "lora"
    return module_str

def extract_metadata_from_safetensor(filepath):
    metadata = {}

    with safe_open(filepath, framework="pt", device="cpu") as f:
        raw_meta = f.metadata()
        if not raw_meta:
            print(f"No metadata found in {filepath}.")
            return {}

        if "ss_steps" in raw_meta:
            metadata["steps"] = int(raw_meta["ss_steps"])

        if "ss_network_dim" in raw_meta:
            try:
                metadata["dim"] = int(raw_meta["ss_network_dim"])
            except ValueError:
                metadata["dim"] = raw_meta["ss_network_dim"]

        if "ss_network_alpha" in raw_meta:
            try:
                metadata["alpha"] = float(raw_meta["ss_network_alpha"])
            except ValueError:
                metadata["alpha"] = raw_meta["ss_network_alpha"]

        if "ss_learning_rate" in raw_meta:
            metadata["learning_rate"] = float(raw_meta["ss_learning_rate"])

        if "ss_base_model_version" in raw_meta:
            metadata["base_model"] = raw_meta["ss_base_model_version"]

        if "ss_mixed_precision" in raw_meta:
            metadata["precision"] = raw_meta["ss_mixed_precision"]

        if "ss_fp8_base" in raw_meta:
            metadata["base_precision"] = "fp8" if raw_meta["ss_fp8_base"] else metadata["precision"]

        if "ss_network_module" in raw_meta:
            metadata["network"] = readable_network_module(raw_meta["ss_network_module"])

        if "ss_min_snr_gamma" in raw_meta:
            min_snr_gamma = raw_meta["ss_min_snr_gamma"]

            # if value is None, set to -1
            if min_snr_gamma == 'None':
                metadata["min_snr_gamma"] = -1
            else:
                metadata["min_snr_gamma"] = float(min_snr_gamma)


        if "ss_num_train_images" in raw_meta:
            metadata["training_images"] = int(raw_meta["ss_num_train_images"])

        if "ss_optimizer" in raw_meta:
            metadata["optimizer_raw"] = raw_meta["ss_optimizer"]
            metadata.update(parse_optimizer(raw_meta["ss_optimizer"]))

        if "ss_network_args" in raw_meta:
            metadata["network_args_raw"] = raw_meta["ss_network_args"]
            metadata.update(parse_network_args(raw_meta["ss_network_args"]))

        if "ss_output_name" in raw_meta:
            output_name = raw_meta["ss_output_name"]
            if "+" in output_name:
                metadata["merge"] = True
                metadata["merged_from"] = output_name.split("+")

    print(f"Extracting metadata from {filepath}: {metadata}")
    return metadata


def hash_safetensor(filepath):
    """
    Generates a SHA256 hash for the .safetensors file
    """
    import hashlib

    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()


def process_folder(folder_path, single_file=False):
    path = Path(folder_path)

    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    if path.is_file() and not single_file:
        path = path.parent

    if single_file:
        files = [path]
    else:
        files = path.rglob("*.safetensors")

    print(f"Processing safetensors in folder: {path}")
    for file in files:
        print(f"Reading {file.name}...")
        meta = extract_metadata_from_safetensor(file)
        if meta:
            hash = hash_safetensor(file)
            meta["hash"] = hash

            json_path = file.with_suffix(".json")
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(meta, f, indent=2)
            print(f"✅ Wrote metadata to {json_path.name}")
        else:
            print(f"⚠️ No metadata found in {file.name}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract metadata from .safetensors files into JSON.")
    parser.add_argument(
        "--single_file",
        action="store_true",
        help="Process a single .safetensors file instead of a folder.",
    )
    parser.add_argument("folder", help="Folder containing .safetensors files.")
    args = parser.parse_args()

    process_folder(args.folder, args.single_file)
