"""
File Organizer Script
Automates moving or copying image files (.jpg, .jpeg) from a source directory to a target directory.
Uses built-in Python modules: os, shutil.
"""

import os
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def move_jpg_files(source_dir: str, destination_dir: str, extensions: tuple = ('.jpg', '.jpeg'), copy_instead: bool = False) -> int:
    """
    Moves (or copies) all JPG/JPEG files from source_dir to destination_dir.

    :param source_dir: Path to the directory containing files.
    :param destination_dir: Path to the target directory where files should be moved.
    :param extensions: Tuple of allowed file extensions (default: ('.jpg', '.jpeg')).
    :param copy_instead: If True, copies files instead of moving them.
    :return: Count of files successfully processed.
    """
    if not os.path.exists(source_dir):
        logging.error(f"Source directory does not exist: '{source_dir}'")
        raise FileNotFoundError(f"Source directory '{source_dir}' not found.")

    if not os.path.isdir(source_dir):
        logging.error(f"Source path is not a directory: '{source_dir}'")
        raise NotADirectoryError(f"'{source_dir}' is not a directory.")

    # Ensure target directory exists
    os.makedirs(destination_dir, exist_ok=True)
    logging.info(f"Target directory ready: '{destination_dir}'")

    processed_count = 0
    # Normalize extensions to lowercase
    lower_exts = tuple(ext.lower() for ext in extensions)

    for item_name in os.listdir(source_dir):
        source_item_path = os.path.join(source_dir, item_name)

        # Skip directories
        if not os.path.isfile(source_item_path):
            continue

        # Check extension
        if item_name.lower().endswith(lower_exts):
            dest_item_path = os.path.join(destination_dir, item_name)
            
            try:
                if copy_instead:
                    shutil.copy2(source_item_path, dest_item_path)
                    logging.info(f"Copied: '{item_name}' -> '{destination_dir}'")
                else:
                    shutil.move(source_item_path, dest_item_path)
                    logging.info(f"Moved: '{item_name}' -> '{destination_dir}'")
                
                processed_count += 1
            except Exception as e:
                logging.error(f"Failed to process '{item_name}': {e}")

    logging.info(f"Task Complete! Total files processed: {processed_count}")
    return processed_count


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Move or copy .jpg files from source to destination directory.")
    parser.add_argument("-s", "--source", required=True, help="Source directory path")
    parser.add_argument("-d", "--destination", required=True, help="Destination directory path")
    parser.add_argument("--copy", action="store_true", help="Copy files instead of moving them")

    args = parser.parse_args()

    try:
        count = move_jpg_files(args.source, args.destination, copy_instead=args.copy)
        print(f"\n[SUCCESS] Processed {count} file(s).")
    except Exception as err:
        print(f"\n[ERROR] {err}")
