import os
import shutil
from tqdm import tqdm
from datetime import datetime

def organize_and_move_files(source_directory, destination_directory):
    # File extensions categorized by type
    image_extensions = ['.jpg', '.png', '.gif', '.bmp', '.jpeg', '.HEIC', '.heic', '.WEBP']
    video_extensions = ['.mov', '.mp4']
    other_extensions = ['.json']

    # Group extensions into categories
    file_categories = {'Images': image_extensions, 'Videos': video_extensions, 'Others': other_extensions}

    total_files = 0

    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Count total number of files to be moved
    for root, _, files in os.walk(source_directory):
        for category, extensions in file_categories.items():
            total_files += sum(1 for file in files if any(file.lower().endswith(ext.lower()) for ext in extensions))

    # Initialize progress bar
    progress_bar = tqdm(total=total_files, desc="Moving files")

    # Start moving files
    for root, _, files in os.walk(source_directory):
        for category, extensions in file_categories.items():
            for file in files:
                if any(file.lower().endswith(ext.lower()) for ext in extensions):
                    # Create subfolder for the file type (Images, Videos, Others)
                    type_subfolder_path = os.path.join(destination_directory, category)
                    if not os.path.exists(type_subfolder_path):
                        os.makedirs(type_subfolder_path)

                    src_path = os.path.join(root, file)

                    # Get file creation time and format it to create date-based subfolder
                    created_time = datetime.fromtimestamp(os.path.getctime(src_path))
                    date_based_folder = created_time.strftime('%y%m_%B')  # YYMM_MonthName format

                    # Create date-based subfolder within the file type subfolder
                    date_based_subfolder_path = os.path.join(type_subfolder_path, date_based_folder)
                    if not os.path.exists(date_based_subfolder_path):
                        os.makedirs(date_based_subfolder_path)

                    # Destination path for the file
                    dest_path = os.path.join(date_based_subfolder_path, file)

                    # Skip if the file already exists at the destination
                    if os.path.exists(dest_path):
                        print(f"Duplicate exists, skipping: {file}")
                        continue

                    # Copy the file and remove the original
                    shutil.copy2(src_path, dest_path)
                    os.remove(src_path)

                    # Update the progress bar
                    progress_bar.update(1)

    # Close the progress bar when done
    progress_bar.close()

# Source and destination folder paths
source_directory = '/Users/mainuser/Desktop/test_source'
destination_directory = '/Users/mainuser/Desktop/test_destination'

# Execute the function to move and organize files
organize_and_move_files(source_directory, destination_directory)
