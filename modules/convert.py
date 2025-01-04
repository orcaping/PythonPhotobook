from pillow_heif import register_heif_opener  # type: ignore
from PIL import Image, UnidentifiedImageError  # type: ignore
import os

# Register HEIF opener to handle HEIC format
register_heif_opener()


def convert_heic_to_jpeg(src_path):
    """
    Convert a single HEIC file to JPEG format.
    Deletes the original HEIC file after conversion.

    Args:
        src_path (str): The full path of the HEIC file to convert.

    Returns:
        str: The path of the converted JPEG file, or None if conversion failed.
    """
    dest_path = os.path.splitext(src_path)[0] + ".jpg"

    if os.path.exists(dest_path):
        print(f"JPEG already exists for {os.path.basename(src_path)}, skipping.")
        return dest_path  # Return the path of the existing JPEG file

    try:
        # Retrieve original file metadata
        original_mtime = os.path.getmtime(src_path)
        original_ctime = os.path.getctime(src_path)

        # Open and convert the HEIC image to JPEG
        with Image.open(src_path) as img:
            img.convert("RGB").save(dest_path, "JPEG")
        print(f"Converted {os.path.basename(src_path)} to {dest_path}")

        # Set the metadata of the JPEG file to match the HEIC file
        os.utime(dest_path, (original_mtime, original_mtime))

        # Delete the original HEIC file
        os.remove(src_path)
        print(f"Deleted original HEIC file: {os.path.basename(src_path)}")
        return dest_path  # Return the path of the new JPEG file

    except UnidentifiedImageError:
        print(f"Failed to convert {os.path.basename(src_path)}: File format not recognized or invalid HEIC file.")
    except Exception as e:
        print(f"Failed to convert {os.path.basename(src_path)}: {e}")

    return None  # Return None if conversion failed
