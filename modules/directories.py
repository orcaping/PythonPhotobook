import os


def validate_paths(source_path: str, destination_path: str) -> None:
    # Check if source path exists and is accessible
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source path '{source_path}' does not exist.")
    if not os.access(source_path, os.R_OK):
        raise PermissionError(f"Source path '{source_path}' is not readable.")

    # Check if destination path exists
    if not os.path.exists(destination_path):
        try:
            os.makedirs(destination_path)
            print(f"Destination path '{destination_path}' did not exist. It has been created.")
        except PermissionError:
            raise PermissionError(f"Cannot create destination path '{destination_path}'. Check permissions.")
    else:
        print(f"Destination path '{destination_path}' already exists.")
