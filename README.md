# OCR Selector

The OCR Selector is a Python script that allows you to easily capture a screenshot, perform optical character recognition (OCR) on the captured image, save the extracted text to a text file, and copy it to the clipboard. 
It is designed to streamline the process of extracting text from images for various purposes such as digitizing documents, extracting text from images, and more.

This script has been made in Ubuntu 22.04 and has not been tested or optimized for other operating systems, although most Debian based OS's should be fine.



## Features

- Downloading Python3.x libraries.
- Capture and update a screenshot of a selected area on the screen.
- Preprocess the captured image for better OCR accuracy.
- Perform OCR using Tesseract OCR engine.
- Save the extracted text to a text file for future reference or reuse.
- Copy the extracted text to the clipboard for immediate use.

## Installation

### Dependencies

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `python3-tk` (for capturing screenshots)
- `tesseract-ocr` (OCR engine)
- `xclip` (for copying text to clipboard)

You can install these dependencies on Ubuntu using the following CLI command in Ubuntu:

- `sudo apt-get install python3-tk python3-dev tesseract-ocr xclip`



### Installing Python Packages

The script also requires several Python packages, it will try to install this itself only one the first run using pip.
They can also manually be installed using pip. Run the following command to install the required packages:

- `pip3 install -r requirements.txt`
or
- `pip install -r requirements.txt`



## Usage

1. Clone the repository to your local machine:

git clone https://github.com/your-username/ocr-toolkit.git


3. Navigate to the project directory:

cd ocr-toolkit


3. Make the script executable and run the script:


python3 ocr_toolkit.py


4. The script will create a transparent overlay on the screen and make a cross of your cursor, select the part you would like to extract into text by dragging a box around it.
Once the screenshot is captured, the extracted text will be saved to a text file and copied to the clipboard automatically.
Extracted text will be saved in `~/Documents/OCR/OCR_history.txt`, original screenshot will be saved as `~/Documents/OCR/OCR_screenshot.png` and the preprocessed screenshot will be saved as `~/Documents/OCR/OCR_screenshot_preprocessed.png`.
This script can also be used as a standard tool for making screenshots, as it updates the screenshot it captures, ensuring that it does not clog up your storage with unnecessary files.


Setting Up the OCR Selector (Optional shortcut)

If you'd like extra convenience of the OCR Selector for your own use, follow these steps:

1. Navigate to the Folder: Open a terminal and navigate to the folder where you downloaded the repository.
    Move Files: Move the files to ~/Documents/OCR/ 
    CLI command would be: - `mv * ~/Documents/OCR/`.

2. Make the File Executable: Right-click on the OCR Selector.desktop file, go to "Properties," and under the "Permissions" tab, check the box that says "Allow executing file as program."
    Or CLI command: 
      - `sudo chmod +x ~/Documents/OCR/OCR\ Selector.desktop`.
      - `sudo chmod +x ~/Documents/OCR/OCRselect.py`.

3. Move the file to your applications folder.
  ~/.local/share/applications/
  Or CLI command:
      - `mv ~/Documents/OCR/OCR\ Selector.desktop ~/.local/share/applications/`.

    If the application is not directly visible you might need to reboot your system.


Launch the OCR Selector: Click on the OCR Selector icon whenever you want to run the script. This shortcut provides easy access to the OCR functionality.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



