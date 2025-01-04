import sys
import os


def integrity_check(source_path, destination_path, IMAGE_EXTENSIONS):
    check_match_filecount(source_path, destination_path, IMAGE_EXTENSIONS)
    check_wrong_fileformat()


def count_files_with_extensions(directory, extensions):
    count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                count += 1
    return count


def check_match_filecount(source_path, destination_path, IMAGE_EXTENSIONS):
    title = " Checking Image File Count Integrity "
    border = "*" * (len(title) + 2)
    print("\n" + border)
    print(f"*{title}*")
    print(border)

    source_file_count = count_files_with_extensions(source_path, IMAGE_EXTENSIONS)
    destination_file_count = count_files_with_extensions(destination_path, IMAGE_EXTENSIONS)

    print(f"Source file count: {source_file_count}")
    print(f"Destination file count: {destination_file_count}")

    if source_file_count == destination_file_count:
        print("\n✅ File count matches! Continuing with checks...\n")
    else:
        print("\n🚩 File count does not match! Stopping further checks...\n")
        sys.exit("Error: File count mismatch.")


def check_wrong_fileformat():
    title = " Checking File Format Integrity "
    border = "*" * (len(title) + 2)
    print("\n" + border)
    print(f"*{title}*")
    print(border)


# if True:
#     print("\n✅ File count matches! Continuing with checks...\n")
# else:
#     print("\n🚩 File count does not match! Stopping further checks...\n")
#     sys.exit("Error: File count mismatch.")
