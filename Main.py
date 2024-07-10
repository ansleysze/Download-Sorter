import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from tkinter import messagebox
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

REQUIRED_FOLDERS = ["Zips", "CSV", "Pics&Images", "PDFs", "Docs", "Music", "Others"]

DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

def create_required_folders():
    for folder in REQUIRED_FOLDERS:
        folder_path = os.path.join(DOWNLOADS_FOLDER, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logging.debug(f"Created folder: {folder_path}")

def main():
    create_required_folders()
    logging.debug("Required folders created")

    observer = Observer()
    handler = FileSorterHandler()
    observer.schedule(handler, DOWNLOADS_FOLDER, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

class FileSorterHandler(FileSystemEventHandler):
    def on_moved(self, event):
        if not event.is_directory:
            file_path = event.dest_path
            file_name, file_extension = os.path.splitext(file_path)
            file_extension = file_extension.lower()

            if file_extension not in [".tmp", ".crdownload", ".part"]:
                self.move_file(file_path, file_extension)

    def move_file(self, file_path, file_extension):
        if file_extension == ".zip":
            destination_folder = "Zips"
        elif file_extension == ".csv":
            destination_folder = "CSV"
        elif file_extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
            destination_folder = "Pics&Images"
        elif file_extension == ".pdf":
            destination_folder = "PDFs"
        elif file_extension in [".doc", ".docx", ".odt"]:
            destination_folder = "Docs"
        elif file_extension in [".mp3", ".wav", ".ogg"]:
            destination_folder = "Music"
        else:
            destination_folder = "Others"

        destination_folder_path = os.path.join(DOWNLOADS_FOLDER, destination_folder)

        try:
            if os.path.exists(file_path):
                if not os.path.exists(os.path.join(destination_folder_path, os.path.basename(file_path))):
                    logging.debug(f"Moving file: {file_path} to {destination_folder_path}")
                    shutil.move(file_path, destination_folder_path)
                    logging.debug(f"File moved successfully: {file_path} to {destination_folder_path}")
                else:
                    logging.debug(f"File already exists in destination folder: {file_path}")
            else:
                logging.debug(f"File does not exist: {file_path}")
        except shutil.Error as e:
            logging.debug(f"Error moving file: {e}")

if __name__ == "__main__":
    main()