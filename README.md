# Download-Sorter
This Python script automatically organizes files downloaded to your Downloads folder into specific subfolders based on their file types. It uses the watchdog library to monitor the Downloads directory and move files to appropriate subfolders as soon as they are downloaded. I made this since I used to download a lot of items in schoolwork so I thought of making this script to make it easy for me to locate where is what

Features
Automatically creates required subfolders if they don't exist.
Monitors the Downloads folder for new files and moves them to subfolders based on their file extensions.
Handles a variety of file types, including:
Zips: .zip
CSV: .csv
Pics&Images: .jpg, .jpeg, .png, .gif, .bmp
PDFs: .pdf
Docs: .doc, .docx, .odt
Music: .mp3, .wav, .ogg
Others: Any other file types
