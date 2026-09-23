import os
import shutil
import logging
from datetime import datetime

LOG_FILE = "organiser_log.txt"
SOURCE   = "C:/Users/Admin/Downloads"

CATEGORIES = {
    ".jpg" : "Images",  ".jpeg": "Images",  ".png" : "Images",  ".gif" : "Images",
    ".pdf" : "Documents",".doc": "Documents",".docx":"Documents",
    ".txt" : "Text",    ".log" : "Text",    ".md"  : "Text",
    ".py"  : "Scripts", ".js"  : "Scripts", ".html": "Scripts",
    ".mp3" : "Media",   ".mp4" : "Media",
    ".zip" : "Archives",".rar" : "Archives",
    ".exe" : "Installers",".msi": "Installers",
}

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(f"  {entry}")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def organise_folder():
    if not os.path.exists(SOURCE):
        log(f"ERROR: Folder not found — {SOURCE}")
        return

    all_files = [
        f for f in os.listdir(SOURCE)
        if os.path.isfile(os.path.join(SOURCE, f))
    ]

    if not all_files:
        log("No files to organise")
        return

    log(f"Started — {len(all_files)} files found in {SOURCE}")
    moved = 0
    skipped = 0
    errors = 0
    category_count = {}
    start = datetime.now()

    for filename in all_files:
        try:
            _, ext     = os.path.splitext(filename)
            ext        = ext.lower()
            category   = CATEGORIES.get(ext, "Others")
            dest_folder= os.path.join(SOURCE, category)
            src        = os.path.join(SOURCE, filename)
            dest       = os.path.join(dest_folder, filename)

            os.makedirs(dest_folder, exist_ok=True)

            if os.path.exists(dest):
                log(f"SKIP    | {filename} already in {category}/")
                skipped += 1
                continue

            shutil.move(src, dest)
            log(f"MOVED   | {filename} -> {category}/")
            moved += 1
            category_count[category] = category_count.get(category, 0) + 1

        except PermissionError:
            log(f"ERROR   | {filename} — Permission denied")
            errors += 1
        except Exception as e:
            log(f"ERROR   | {filename} — {e}")
            errors += 1

    elapsed = (datetime.now() - start).total_seconds()
    print("\n  " + "="*50)
    print("  ORGANISATION COMPLETE")
    print("  " + "="*50)
    print(f"  Moved    : {moved}")
    print(f"  Skipped  : {skipped}")
    print(f"  Errors   : {errors}")
    print(f"  Time     : {elapsed:.2f} seconds")
    print(f"\n  Files by category:")
    for cat, count in sorted(category_count.items(), key=lambda x: x[1], reverse=True):
        bar = "#" * count
        print(f"  {cat:<12} {bar} ({count})")
    print("  " + "="*50)
    log(f"Done — {moved} moved, {skipped} skipped, {errors} errors in {elapsed:.2f}s")

def main():
    print("\n" + "="*50)
    print("  FILE ORGANISER AUTOMATION TOOL")
    print("  Built by: S. Mukesh Kumar")
    print("="*50)
    organise_folder()

main()