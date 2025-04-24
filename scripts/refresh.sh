#!/bin/bash

# Path to your content directory where images are stored
CONTENT_DIR="./content"

# Path to the Python EXIF extraction script
EXIF_SCRIPT="./scripts/extract_png_metadata.py"
TENSOR_SCRIPT="./scripts/extract_safetensors_metadata.py"

# Function to refresh metadata
refresh_metadata() {
  find "$CONTENT_DIR" \( -iname '*.png' -o -iname '*.safetensors' \) | while read file; do
    json_file="${file%.*}.json"

    if [[ ! -f "$json_file" || "$file" -nt "$json_file" ]]; then
      echo "Refreshing metadata for: $file"

      if [[ "$file" == *.png ]]; then
        echo "→ Running EXIF script: $EXIF_SCRIPT"
        python "$EXIF_SCRIPT" "$file"
      elif [[ "$file" == *.safetensors ]]; then
        echo "→ Running Tensor script: $TENSOR_SCRIPT"
        python "$TENSOR_SCRIPT" "$file"
      fi
    else
      echo "✓ JSON is up to date: $json_file"
    fi
  done
}

refresh_metadata
