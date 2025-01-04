### File Organization Tool Guide

This document provides simple instructions for using the File Organization Tool to sort, convert, and validate image files.

---

## **Features**
1. **Organize Images**: Sort image files into date-based folders (e.g., `2023/January/01`).
2. **Convert Formats**: Automatically convert `.heic` images to `.jpeg` if specified.
3. **Integrity Check**: Validate the integrity of the organized files by ensuring file counts match.
4. **Dry-Run**: Simulate the process without making actual changes to your files.

---

## **Requirements**

### **Python Version**
- Python 3.7 or newer.

## **Installing Python**

### **Windows**
1. **Download Python**
   - Go to the [official Python website](https://www.python.org/downloads/).
   - Download the latest version for Windows.

2. **Install Python**
   - Run the downloaded installer.
   - Ensure the **"Add Python to PATH"** checkbox is selected during installation.
   - Choose **"Install Now"** for the default settings.

3. **Verify Installation**
   - Open Command Prompt (`Win + R`, type `cmd`, and press Enter).
   - Run:
     ```bash
     python --version
     ```
   - You should see the installed Python version.

4. **Install Pip**
   - Pip is included by default in modern Python versions. Verify it with:
     ```bash
     pip --version
     ```

### **macOS**
1. **Download Python**
   - Visit the [official Python website](https://www.python.org/downloads/).
   - Download the macOS version.

2. **Install Python**
   - Open the downloaded `.pkg` file and follow the on-screen instructions.

3. **Verify Installation**
   - Open Terminal (`Cmd + Space`, type `Terminal`, and press Enter).
   - Run:
     ```bash
     python3 --version
     ```
   - macOS uses `python3` instead of `python`.

4. **Install Pip**
   - Pip is included by default. Verify it with:
     ```bash
     pip3 --version
     ```
---

### **Python Packages**
The tool depends on the following Python libraries:
- `pillow_heif`
- `Pillow`
- `tqdm`

You can install these dependencies using:
```bash
pip install -r requirements.txt
```

---

## **Usage**

### **Running the Tool**
Run the script using the terminal:
```bash
python photobook.py -s <source_directory> -d <destination_directory> [options]
```

### **Options**
| **Option**           | **Description**                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------|
| `-s`, `--source`      | Source directory containing files to organize. **(Required)**                                       |
| `-d`, `--destination` | Destination directory to store organized files. **(Required)**                                      |
| `--dry-run`           | Simulate the organization process without actually moving or copying files.                         |
| `-c`, `--convert`     | Convert `.heic` files to `.jpeg` before sorting.                                                    |
| `--log-to-file`       | Log operations to a file in the destination directory.                                              |
| `-i`, `--integrity-check` | Check if the source and destination directories have matching file counts after processing. |

---

## **Examples**

### **Basic Sorting**
```bash
python photobook.py -s /path/to/source -d /path/to/destination
```

### **Sorting with Conversion**
```bash
python photobook.py -s /path/to/source -d /path/to/destination -c
```

### **Dry-Run Mode**
```bash
python photobook.py -s /path/to/source -d /path/to/destination --dry-run
```

### **With Integrity Check**
```bash
python photobook.py -s /path/to/source -d /path/to/destination -i
```

---

## **Output Structure**
Organized files will be saved in a structured format:
```
/destination_directory
└── Images
    ├── 2023_January
    │   └── 2023-01-01
    │       ├── image1.jpg
    │       └── image2.png
    └── Unsorted_Files
        └── <File Type>
            └── unsorted_file1.ext
```

---

## **Error Handling**

- **Invalid Paths**: If a source or destination directory is missing, the tool will alert you and halt execution.
- **File Count Mismatch**: During integrity checks, the tool stops processing if the source and destination counts do not match.
- **HEIC Conversion Failure**: If a `.heic` file fails to convert, it will remain in the unsorted folder.

---

## **Additional Resources**
- [Python Documentation](https://docs.python.org/3/)
- [Installing Python on Windows](https://docs.python.org/3/using/windows.html)
- [Installing Python on macOS](https://docs.python.org/3/using/mac.html)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)