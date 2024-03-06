# ocr_selector
OCR tool for quickly capturing non-selectable text

# OCR Toolkit

The OCR Toolkit is a Python script that allows you to easily capture a screenshot, perform optical character recognition (OCR) on the captured image, save the extracted text to a text file, and copy it to the clipboard. It is designed to streamline the process of extracting text from images for various purposes such as digitizing documents, extracting text from images, and more.

## Features

- Capture a screenshot of a selected area on the screen.
- Preprocess the captured image for better OCR accuracy.
- Perform OCR using Tesseract OCR engine.
- Save the extracted text to a text file for future reference.
- Copy the extracted text to the clipboard for immediate use.

## Installation

### Dependencies

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `python3-tk` (for capturing screenshots)
- `tesseract-ocr` (OCR engine)
- `xclip` (for copying text to clipboard)

You can install these dependencies on Ubuntu using the following CLI command:
"""
sudo apt-get install python3-tk python3-dev tesseract-ocr xclip
"""


### Installing Python Packages

The script also requires several Python packages, which can be installed using pip. Run the following command to install the required packages:
pip install -r requirements.txt
or
pip3 install -r requirements.txt



## Usage

1. Clone the repository to your local machine:
2. 
git clone https://github.com/your-username/ocr-toolkit.git


3. Navigate to the project directory:

cd ocr-toolkit


3. Run the script:

python ocr_toolkit.py


4. Follow the on-screen instructions to capture a screenshot. Once the screenshot is captured, the extracted text will be saved to a text file and copied to the clipboard automatically.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



