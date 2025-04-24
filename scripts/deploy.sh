hugo --gc --minify 
rclone sync --progress --exclude '*.safetensors' public/ hugo-thalis:thalis-site/
rclone sync --progress --include '*.safetensors' public/ hugo-thalis:thalis-downloads/
