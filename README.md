# Download-Sorter
This Python script automatically organizes files downloaded to your Downloads folder into specific subfolders based on their file types. It uses the watchdog library to monitor the Downloads directory and move files to appropriate subfolders as soon as they are downloaded. I made this since I used to download a lot of items in schoolwork so I thought of making this script to make it easy for me to locate items.

Version 1.0.0

## Features

Automatically creates required subfolders if they don't exist.
Monitors the Downloads folder for new files and moves them to subfolders based on their file extensions.    Handles a variety of file types, including: 

Zips: .zip   
CSV: .csv   
Pics&Images: .jpg, .jpeg, .png, .gif, .bmp  
PDFs: .pdf   
Docs: .doc, .docx, .odt   
Music: .mp3, .wav, .ogg  
Others: Any other file types   

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/file-organizer.git
    cd file-organizer
    ```

2. **Install the required packages:**
    ```bash
    pip install watchdog
    ```

## Usage

Run the script to start organizing your files using Python 3:

```bash
python file_organizer.py
```

The script will automatically create the required folders in your Downloads directory if they do not already exist. It will then monitor the Downloads folder and move files to their appropriate subfolders as they are downloaded.

## Updates

1.0 Base Sorting works will update soon

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes. 

All contributions are welcome!



## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. 

