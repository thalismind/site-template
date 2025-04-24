#!/bin/bash

# Path to your content directory where images are stored
CONTENT_DIR="./content"

# Path to the Python EXIF extraction script
EXIF_SCRIPT="./scripts/extract_png_metadata.py"
TENSOR_SCRIPT="./scripts/extract_safetensors_metadata.py"

# Function to handle cleanup when the script is stopped
cleanup() {
  echo "Cleaning up... Exiting processes."
  kill "$hugo_pid"  # Kill the hugo server process
  wait "$hugo_pid"   # Wait for the hugo process to exit
  exit 0
}

# Set up the trap to catch INT and TERM signals and call cleanup
trap cleanup INT TERM

# Start the Hugo server in the background (only once)
hugo server --watch -D &
hugo_pid=$!  # Store the hugo process ID

# Function to watch the content directory and run the EXIF extraction script
watch_directory() {
  echo "Watching directory: $CONTENT_DIR for changes..."

  # Use inotifywait to watch for any new files or modifications in the content directory
  inotifywait -m -r -e create -e modify --format '%w%f' "$CONTENT_DIR" | while read file; do
    # Print the file that triggered the event
    echo "File changed: $file"

    # Check if the modified or created file is a PNG
    if [[ "$file" == *.png ]]; then
      echo "Detected change in image: $file"
      python "$EXIF_SCRIPT" "$file"  # Run the EXIF extraction script
    fi

    if [[ "$file" == *.safetensors ]]; then
      echo "Detected change in tensor: $file"
      python "$TENSOR_SCRIPT" "$file"  # Run the Safetensors extraction script
    fi
  done
}

# Start the inotifywait watch in the background
watch_directory &
watch_pid=$!  # Store the inotifywait process ID

# Wait for the Hugo server and inotifywait processes to complete
wait "$hugo_pid" "$watch_pid"
