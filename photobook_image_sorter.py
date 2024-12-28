import os
import shutil
from tqdm import tqdm
from datetime import datetime
import sys
import argparse

class Tee:
    """A simple class to write output to both console and a log file."""
    def __init__(self, log_file):
        self.log_file = open(log_file, "w")
        self.console = sys.stdout

    def write(self, message):
        self.console.write(message)
        self.log_file.write(message)

    def flush(self):
        self.console.flush()
        self.log_file.flush()

    def close(self):
        self.log_file.close()


def validate_directories(source_directory, destination_directory):
    """Ensure source and destination directories are accessible."""
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory not found: {source_directory}")
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

def organize_and_move_files(source_directory, destination_directory, dry_run=False):
    # File extensions categorized by type
    image_extensions = ['.jpg', '.png', '.gif', '.bmp', '.jpeg', '.HEIC', '.heic', '.WEBP']

    total_files = 0

    # Validate directories
    validate_directories(source_directory, destination_directory)

    # Create "Unsorted" folder for files that don't match extensions
    unsorted_folder = os.path.join(destination_directory, "Unsorted_Files")
    if not os.path.exists(unsorted_folder):
        os.makedirs(unsorted_folder)

    # Count total number of image files to be moved
    for root, _, files in os.walk(source_directory):
        for file in files:
            if file.startswith('.'):  # Skip hidden files
                continue
            if any(file.lower().endswith(ext.lower()) for ext in image_extensions):
                total_files += 1

    # Debug: Print total files found
    print(f"Total image files found: {total_files}")

    # Initialize progress bar only if there are files to move
    if total_files > 0:
        progress_bar = tqdm(total=total_files, desc="Moving image files")
    else:
        print("No image files found to move.")
        return  # Exit the function if no files are found

    # Start moving files
    for root, _, files in os.walk(source_directory):
        for file in files:
            if file.startswith('.'):  # Skip hidden files
                continue

            src_path = os.path.join(root, file)

            if any(file.lower().endswith(ext.lower()) for ext in image_extensions):
                # Handle image files
                modified_time = datetime.fromtimestamp(os.path.getmtime(src_path))
                year_month_folder = modified_time.strftime('%Y%m_%B')  # YYYYMM_MonthName format
                date_folder = modified_time.strftime('%Y-%m-%d')  # YYYY-MM-DD format

                type_subfolder_path = os.path.join(destination_directory, "Images")
                year_month_path = os.path.join(type_subfolder_path, year_month_folder)
                if not os.path.exists(year_month_path):
                    os.makedirs(year_month_path)

                date_path = os.path.join(year_month_path, date_folder)
                if not os.path.exists(date_path):
                    os.makedirs(date_path)

                dest_path = os.path.join(date_path, file)

            else:
                # Handle unsorted files
                file_extension = os.path.splitext(file)[1].lower()
                extension_folder = os.path.join(unsorted_folder, file_extension[1:].upper() if file_extension else "Unknown")
                if not os.path.exists(extension_folder):
                    os.makedirs(extension_folder)
                dest_path = os.path.join(extension_folder, file)

            # Skip if the file already exists at the destination
            if os.path.exists(dest_path):
                print(f"Duplicate exists, skipping: {file}")
                continue

            if dry_run:
                print(f"DRY RUN: Would copy {src_path} to {dest_path}")
                continue

            # Copy the file (uncomment os.remove for production version)
            shutil.copy2(src_path, dest_path)

            if any(file.lower().endswith(ext.lower()) for ext in image_extensions):
                # Update progress bar for image files only
                progress_bar.update(1)

    # Close the progress bar when done
    progress_bar.close()

    # Print completion message
    print(f"Copying completed. You can find sorted files in the folder: {destination_directory}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize and move files based on their modification date.")
    parser.add_argument("source", help="Source directory containing the files to organize.")
    parser.add_argument("destination", help="Destination directory to move organized files to.")
    parser.add_argument("--dry-run", action="store_true", help="Simulate the organization process without moving files.")

    args = parser.parse_args()

    # Set up logging to both console and file
    log_timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(args.destination, f"log_{log_timestamp}.txt")
    tee = Tee(log_file)
    sys.stdout = tee
    sys.stderr = tee

    # Execute the function to move and organize files
    try:
        organize_and_move_files(args.source, args.destination, dry_run=args.dry_run)
    finally:
        tee.close()
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
