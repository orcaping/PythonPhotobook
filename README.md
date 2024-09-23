# 📁 Organize and Move Files by Type & Date

A powerful script to help you organize and move files from a source directory to a destination directory. This script categorizes files into types (e.g., Images, Videos, Others) and further organizes them into date-based subfolders based on the creation date of each file. It supports various file types, including common image and video formats, and provides real-time feedback with a progress bar.

---

## 🌟 Key Features
- **File Type Organization**: Automatically categorizes files into folders like "Images", "Videos", and "Others" based on file extensions.
- **Date-Based Subfolder Creation**: Each file is sorted into subfolders by its creation date (formatted as `YYMM_MonthName`, e.g., `2409_September`).
- **Duplicate Handling**: Automatically skips moving files that already exist in the destination, avoiding duplicate content.
- **Real-Time Progress Bar**: Provides a visual representation of file transfer progress using `tqdm`.
- **Extensible & Customizable**: Easily modify the file types and date format according to your needs.

---

## 🛠️ Usage Instructions

### 1. **Install Requirements**
Ensure that you have the required Python packages installed. You can do this by running:

```bash
pip install tqdm
```

### 2. **Running the Script**

To use the script, simply define the source and destination directories and call the `organize_and_move_files()` function:

```python
source_directory = '/path/to/source/folder'
destination_directory = '/path/to/destination/folder'

organize_and_move_files(source_directory, destination_directory)
```

The script will automatically categorize the files in your source folder, organize them by their creation date, and move them into appropriately structured folders in the destination directory.

---

## ⚙️ Customization

The script is designed to be flexible and easily customizable. Below are the different parameters and sections of the code you can modify according to your preferences:

### 1. **File Extensions**
The script categorizes files into three groups: Images, Videos, and Others. You can modify or add new extensions in the following part of the code:

```python
image_extensions = ['.jpg', '.png', '.gif', '.bmp', '.jpeg', '.HEIC', '.heic', '.WEBP']
video_extensions = ['.mov', '.mp4']
other_extensions = ['.json']
```

- **Add New File Types**: If you'd like to categorize additional file types, simply add more extensions to the appropriate list.
- **Create New Categories**: You can also create new categories, such as "Documents" or "Audio", by adding more entries to the `file_categories` dictionary.

### 2. **Date-Based Organization**
Files are placed into subfolders named according to their creation date, using the format `YYMM_MonthName`. You can adjust this date format:

```python
date_based_folder = created_time.strftime('%y%m_%B')  # YYMM_MonthName format
```

- For example, to format dates as `YYYY_MM_Day`, modify the string to:
  ```python
  date_based_folder = created_time.strftime('%Y_%m_%d')
  ```

### 3. **Progress Bar**
The script uses `tqdm` to display a progress bar during the file-moving process. If you'd like to adjust the progress bar or remove it, you can modify this section of the code:

```python
progress_bar = tqdm(total=total_files, desc="Moving files")
```

### 4. **Source and Destination Directories**
You can change the paths for the source and destination directories in the script, or pass them dynamically as arguments.

### 5. **Duplicate File Handling**
By default, the script checks if a file already exists in the destination and skips it if a duplicate is found. You can change this behavior by adjusting this section of the code:

```python
if os.path.exists(dest_path):
    print(f"Duplicate exists, skipping: {file}")
    continue
```

---

## 📂 Directory Structure

After running the script, the destination directory will be organized as follows:

```
/Destination
    /Images
        /2409_September
            image1.jpg
            image2.png
    /Videos
        /2409_September
            video1.mp4
    /Others
        /2409_September
            config.json
```

---

## 🛡️ Error Handling
The script is designed to handle common errors like:
- **File Already Exists**: Skips duplicates to prevent overwriting.
- **Directory Not Found**: Automatically creates missing directories in the destination.
- **Unsupported Extensions**: Files with unsupported extensions are ignored unless new categories are defined.

---

## ✨ Example Use Case
This script is perfect for photographers, videographers, or anyone who deals with large sets of media files. Whether you're organizing personal photos, archiving video projects, or managing client files, this tool can streamline your workflow by automatically sorting and moving files into structured directories.

---

## 🔧 Requirements
- **Python 3.x**
- **Modules**: `tqdm`, `shutil`, `os`, `datetime`

---

## 👨‍💻 Author
This script was developed to automate file organization and enhance productivity. Feel free to modify and adapt it to your needs!

---

By using this script, you’ll never have to manually sort and move files again. Keep your folders neat, organized, and sorted by date with ease!

---

### 🚀 Get started today and take control of your file organization!

