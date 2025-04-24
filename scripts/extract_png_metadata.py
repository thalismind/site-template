import json
from pathlib import Path
from PIL import Image

def parse_parameters(parameters_str):
    """
    Parses the comma-delimited Parameters string into a dict.
    Handles known fields: Steps, CFG, Seed, Hashes.
    """
    result = {}
    lines = parameters_str.split("\n")
    print(f"Parsing parameters: {lines}")

    result["prompt"] = lines[0].strip()
    result["negative_prompt"] = lines[1].strip()

    parts = lines[2].split(",")
    for part in parts:
        part = part.strip()
        if part.startswith("Steps:"):
            result["steps"] = int(part.split(":", 1)[1].strip())
        elif part.startswith("CFG scale:"):
            # CFG of 1.0 is invalid, omit it
            if "1.0" not in part:
                result["cfg"] = float(part.split(":", 1)[1].strip())
        elif part.startswith("Seed:"):
            result["seed"] = part.split(":", 1)[1].strip()
        elif part.startswith("Hashes:"):
            try:
                json_part = part.split(":", 1)[1].strip()
                result["hashes"] = json.loads(json_part)
            except Exception:
                result["hashes"] = {"raw": json_part}
    return result


def extract_metadata(image_path):
    image = Image.open(image_path)
    metadata = {
        "parameters": {},
        "comment": "",
    }

    # Read PNG info fields (tEXt, iTXt)
    info = image.info
    print(f"Extracting metadata from {image}: {info}")

    # Prompt (stored as JSON in your example)
    if "prompt" in info:
        metadata["prompt_raw"] = info["prompt"]
        try:
            prompt_json = json.loads(info["prompt"])
            # Example: get dimensions from EmptySD3LatentImage
            for node in prompt_json.values():
                if node.get("class_type") == "EmptySD3LatentImage":
                    metadata["base_width"] = node["inputs"].get("width")
                    metadata["base_height"] = node["inputs"].get("height")

                if node.get("class_type") == "FluxGuidance":
                    metadata["cfg"] = node["inputs"].get("guidance")

        except Exception as e:
            print(f"Error parsing Prompt JSON: {e}")

    # Parameters
    if "parameters" in info:
        metadata["parameters_raw"] = info["parameters"]
        parsed_params = parse_parameters(info["parameters"])
        metadata.update(parsed_params)

        # Extract initial text prompt from Parameters string
        metadata["parameters"] = info["parameters"].split(".Negative")[0].strip()

    # Comment
    if "comment" in info:
        metadata["comment"] = info["comment"]

    return metadata


def process_folder(folder_path):
    path = Path(folder_path)

    # if path does not exist, raise an error
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")

    # if path ends with a file name, get the parent directory
    if path.is_file():
        path = path.parent

    print(f"Processing folder: {path}")
    for img_file in path.rglob("*.png"):
        print(f"Processing {img_file.name}...")
        meta = extract_metadata(img_file)
        json_path = img_file.with_suffix(".json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2)
        print(f"✅ Wrote metadata for {img_file.name} to {json_path.name}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract Prompt/Parameters/Comment from PNG metadata into JSON.")
    parser.add_argument("folder", help="Folder containing PNG images.")
    args = parser.parse_args()

    print(f"Extracting metadata from PNG files in {args}")

    process_folder(args.folder)
