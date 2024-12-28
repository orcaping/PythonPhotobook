### Organize and Move Files by Type & Date

A straightforward script to help organize and move files from a source directory to a destination directory. This script categorizes files into types (e.g., Images) and organizes them into date-based subfolders based on the last modified date. It is designed to be simple and efficient, with real-time feedback.

---

## Key Features
- **File Type Organization**: Automatically sorts files into predefined categories (e.g., "Images", "Unsorted").
- **Date-Based Subfolders**: Files are further organized into subfolders based on their last modified date, e.g., `YYYYMM_MonthName/YYY-MM-DD`.
- **Duplicate Handling**: Skips moving files that already exist in the destination directory.
- **Dry Run Mode**: Simulates the process without making any changes.
- **Progress Bar**: Displays real-time progress.

---

## How to Use

### 1. Install Requirements
Ensure you have Python 3.x installed along with the required package:

```bash
pip install tqdm
```

### 2. Run the Script
Run the script with the following command:

```bash
python photobook_image_sorter.py /path/to/source /path/to/destination
```

- Replace `/path/to/source` with the folder containing files you want to organize.
- Replace `/path/to/destination` with the folder where files will be organized.

### Optional: Dry Run
To simulate the process without moving files, add the `--dry-run` flag:

```bash
python photobook_image_sorter.py /path/to/source /path/to/destination --dry-run
```

---

## Example Output Structure
After running the script, your destination directory will be organized as follows:

```
/destination
    /Images
        /202412_December
            /2024-12-28
                file1.jpg
                file2.png
    /Unsorted_Files
        /TXT
            notes.txt
        /Unknown
            somefile
```

---

## Notes
1. **Supported File Types**: Currently, only image files (`.jpg`, `.png`, etc.) are categorized under "Images". Other files are placed in the "Unsorted_Files" folder.
2. **Hidden Files**: Files starting with a dot (`.`) are skipped by default.
3. **Logging**: Logs are saved in the destination directory with a timestamp, e.g., `log_YYYYMMDD_HHMMSS.txt`.
4. **Error Handling**: The script creates missing directories and gracefully handles duplicates.

---

## Requirements
- Python 3.x
- `tqdm` module

---

This script is ideal for organizing large sets of media files with minimal effort. Whether you’re managing personal photos or client projects, it simplifies your workflow and keeps your folders clean and organized.