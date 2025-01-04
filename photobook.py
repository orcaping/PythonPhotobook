import argparse
from modules.directories import validate_paths
from modules.sorting import image_sorting
from modules.integrity import integrity_check


def main():
    parser = argparse.ArgumentParser(description="Organize and manage files with additional features.")
    parser.add_argument("-s", "--source", required=True, help="Source path")
    parser.add_argument("-d", "--destination", required=True, help="Destination path")
    parser.add_argument("--dry-run", action="store_true", help="Simulate the organization process without moving files.")
    parser.add_argument("-c", "--convert", action="store_true", help="Convert HEIC files to JPEG before organizing.")
    parser.add_argument("--log-to-file", action="store_true", help="Enable logging to a file in the destination directory.")
    parser.add_argument("-i", "--integrity-check", action="store_true", help="Enable integrity check for copied files")

    args = parser.parse_args()  # noqa

    IMAGE_EXTENSIONS = ['.JPG', '.jpg', '.png', '.gif', '.bmp', '.jpeg', '.heic', '.webp']

    try:
        validate_paths(args.source, args.destination)
        print("Paths are validated successfully!")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")

    if args.integrity_check:
        print("Integrity check is enabled. Running integrity check...")
        integrity_check(args.source, args.destination, IMAGE_EXTENSIONS)
    else:
        print("Sorting files...")
        image_sorting(args.source, args.destination, IMAGE_EXTENSIONS, args.dry_run, args.convert)


if __name__ == "__main__":
    main()
