# File Organiser Automation Tool

A Python automation tool that organizes files into categories automatically using `os` and `shutil`. Includes timestamped logging for every operation.

## Features

- Scans a folder and identifies all files
- Categorizes files by extension (Images, Documents, Scripts, Media, etc.)
- Creates category folders automatically
- Moves files into correct folders
- Logs every operation with timestamp
- Handles errors gracefully (permission denied, file in use)

## Tech Stack

- Python 3.x
- os (folder operations)
- shutil (file moving)
- logging (operation tracking)
- datetime (timestamps)

## How It Works

1. Scans source folder using `os.listdir()`
2. Gets file extension using `os.path.splitext()`
3. Finds category from `CATEGORIES` dictionary
4. Creates folder using `os.makedirs()`
5. Moves file using `shutil.move()`
6. Logs every action with timestamp

## Categories Supported

- Images: .jpg, .jpeg, .png, .gif
- Documents: .pdf, .doc, .docx
- Text: .txt, .log, .md
- Scripts: .py, .js, .html
- Media: .mp3, .mp4
- Archives: .zip, .rar
- Installers: .exe, .msi

## Installation

git clone https://github.com/mukesh-mlops/file-organiser.git
cd file-organiser
python file_organiser.py

## Built By

S. Mukesh Kumar
GitHub: https://github.com/mukesh-mlops
