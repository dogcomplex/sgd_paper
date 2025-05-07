import base64
import sys
import os

def image_to_base64_data_uri(filepath):
    """Converts an image file to a base64 data URI."""
    try:
        # Determine the image type from the file extension
        ext = os.path.splitext(filepath)[1].lower()
        if ext == '.png':
            mime_type = 'image/png'
        elif ext in ['.jpg', '.jpeg']:
            mime_type = 'image/jpeg'
        elif ext == '.gif':
            mime_type = 'image/gif'
        elif ext == '.svg':
            mime_type = 'image/svg+xml'
        else:
            print(f"Error: Unsupported file type '{ext}'. Please use PNG, JPG, GIF, or SVG.", file=sys.stderr)
            return None

        with open(filepath, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:{mime_type};base64,{encoded_string}"
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python img_to_b64.py <image_filepath1> [image_filepath2 ...]", file=sys.stderr)
        sys.exit(1)

    for filepath in sys.argv[1:]:
        data_uri = image_to_base64_data_uri(filepath)
        if data_uri:
            base_filename = os.path.basename(filepath)
            output_filename = os.path.splitext(base_filename)[0] + ".txt"
            try:
                with open(output_filename, "w") as outfile:
                    outfile.write(data_uri)
                print(f"Saved base64 data for '{base_filename}' to '{output_filename}'")
            except Exception as e:
                print(f"Error writing to file {output_filename}: {e}", file=sys.stderr) 