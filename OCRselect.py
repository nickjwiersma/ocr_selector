#!/usr/bin/env python3
# extra dependencies: sudo apt-get install python3-tk python3-dev tesseract-ocr xclip
# Will update last picture in ~/Documents/OCR
# Creates and appends text to a txt file to store OCR history in ~/Documents/OCR/OCR_history.txt
# Copy text to clipboard

# Importing necessary libraries
import pytesseract
import tkinter as tk
from PIL import ImageGrab, Image, ImageEnhance, ImageFilter, ImageOps
import os
import sys # only on first run
import subprocess # only on first run
import pyperclip
import time
print("Imported libraries.")

# Function to check and install required dependencies # only on first run
def install_dependencies(): # only on first run
    """ # only on first run
    Function to install required dependencies using pip. # only on first run
    """ # only on first run
    print("Installing dependencies.") # only on first run
    required_packages = ["Pillow", "pytesseract", "pyperclip"] # only on first run
    for package in required_packages: # only on first run
        try: # only on first run
            subprocess.check_call([sys.executable, "-m", "pip", "install", package]) # only on first run
        except subprocess.CalledProcessError: # only on first run
            print(f"Error: Failed to install {package}.") # only on first run
    print("Done installing dependencies") # only on first run


    # Commenting out lines ending with "# only on first run"
    script_path = os.path.abspath(__file__) # only on first run
    with open(script_path, 'r') as file: # only on first run
        lines = file.readlines() # only on first run
    with open(script_path, 'w') as file: # only on first run
        for line in lines: # only on first run
            if line.strip().endswith("# only on first run"): # only on first run
                file.write("#" + line) # only on first run
            else: # only on first run
                file.write(line) # only on first run

# Function to preprocess the image for better OCR
def preprocess_image(image_path):
    """
    Preprocesses an image by opening it, converting to grayscale, 
    conditionally inverting colors based on brightness, enhancing contrast, 
    applying optional filters, saving the preprocessed image, and returning 
    the path to the preprocessed image.

    Parameters:
    image_path (str): The file path of the input image.

    Returns:
    str: The file path of the preprocessed image.
    """
    # Open the image
    image = Image.open(image_path)
    
    # Convert to grayscale
    grayscale_image = image.convert('L')
    
    # Conditionally invert colors if the image is predominantly dark
    # Calculate the average brightness of the image
    histogram = grayscale_image.histogram()
    pixels = sum(histogram)
    brightness = sum(i * w for i, w in enumerate(histogram)) / pixels

    # If the image is predominantly dark, invert the colors
    if brightness < 128:
        grayscale_image = ImageOps.invert(grayscale_image)
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(grayscale_image)
    enhanced_image = enhancer.enhance(6.0)  # Factor may need adjustment
    
    # Optionally apply a slight blur or other filters
    final_image = enhanced_image.filter(ImageFilter.SMOOTH)
    
    # Save or return the preprocessed image
    preprocessed_path = image_path.replace('.png', '_preprocessed.png')
    final_image.save(preprocessed_path)
    
    return preprocessed_path

# Function to capture a screenshot
def capture_screenshot():
    """
    Captures a screenshot of a selected area on the screen and saves it to a specified directory.
    No parameters.
    Returns the file path of the saved screenshot.
    """
    try:
        print("Starting screenshot capture.")
        root = tk.Tk()
        root.attributes('-fullscreen', True)  # Fullscreen window
        root.attributes('-topmost', True)  # Always on top

        # Wait for the window to become visible to ensure correct application of transparency
        root.wait_visibility(root)
        root.wm_attributes('-alpha', 0.3)  # Adjust transparency level

        selection = {}

        def on_click(event):
            """
            A function to handle the on_click event and initialize start coordinates.
            Parameters:
                event: the event object containing information about the click event.
            Returns:
                None
            """
            # Initialize start coordinates
            selection['start_x'] = event.x_root
            selection['start_y'] = event.y_root

        def on_drag(event):
            """
            Update the selection rectangle as the mouse moves
            """
            # Update the selection rectangle as the mouse moves
            curX, curY = event.x_root, event.y_root
            startX, startY = selection['start_x'], selection['start_y']

            # Remove the previous rectangle
            if 'rectangle' in selection:
                root.canvas.delete(selection['rectangle'])

            # Draw new rectangle
            selection['rectangle'] = root.canvas.create_rectangle(startX, startY, curX, curY, outline='red', fill='', dash=(4, 4))

        def on_release(event):
            """
            Set end coordinates and close the window
            """
            # Set end coordinates and close the window
            selection['end_x'] = event.x_root
            selection['end_y'] = event.y_root
            root.quit()  # Use root.quit() to end the mainloop without destroying the window yet

        # Setting up the canvas with a slight modification for visibility
        root.canvas = tk.Canvas(root, cursor="cross", bg='grey', highlightthickness=0)
        root.canvas.pack(fill=tk.BOTH, expand=True)

        root.canvas.bind('<ButtonPress-1>', on_click)
        root.canvas.bind('<B1-Motion>', on_drag)
        root.canvas.bind('<ButtonRelease-1>', on_release)

        root.mainloop()
        root.destroy()  # Now close (destroy) the window after ending mainloop

        time.sleep(0.5)  # Slight delay to ensure the overlay is fully cleared before capturing

        # Correcting coordinates to ensure they are in the proper order
        left = min(selection['start_x'], selection['end_x'])
        upper = min(selection['start_y'], selection['end_y'])
        right = max(selection['start_x'], selection['end_x'])
        lower = max(selection['start_y'], selection['end_y'])

        # Capture the area selected by the user
        image = ImageGrab.grab(bbox=(left, upper, right, lower))
        print("Screenshot captured.")

        # Save the image
        save_path = os.path.expanduser('~/Documents/OCR/')
        os.makedirs(save_path, exist_ok=True)  # Ensure the directory exists
        file_path = os.path.join(save_path, 'screenshot.png')
        image.save(file_path)
        print(f"Screenshot saved to {file_path}")
        return file_path
    except Exception as e:
        print(f"Error: Failed to capture screenshot: {e}")
        return None

# Function to perform OCR on the captured image
def image_to_text(image_path):
    """
    A function to convert an image to text using OCR.
    
    Args:
        image_path (str): The file path of the input image.
        
    Returns:
        str: The extracted text from the image after OCR processing.
    """
    print("Starting OCR.")
    try:
        # Preprocess the image to improve OCR accuracy
        preprocessed_path = preprocess_image(image_path)

        # Specify the Tesseract command
        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

        # Perform OCR using pytesseract on the preprocessed image
        ocr_text = pytesseract.image_to_string(Image.open(preprocessed_path), config='--psm 6 --oem 3')

        # Remove form feed character from OCR text
        clean_text = ocr_text.replace('\f', '')

        print("OCR complete.")
        return clean_text
    except Exception as e:
        print(f"Error: OCR process failed: {e}")
        return None


# Function to save text to an RTF file
def save_text_to_rtf(text):
    """
    Saves the given text to an txt file.

    Args:
        text (str): The text to be saved to the file.

    Returns:
        None
    """
    try:
        print("Saving text to txt file.")
        ocr_folder_path = os.path.expanduser('~/Documents/OCR/')
        if not os.path.exists(ocr_folder_path):
            os.makedirs(ocr_folder_path)
        file_path = os.path.join(ocr_folder_path, 'OCR_history.txt')
        with open(file_path, 'a') as file:
            file.write(text + '\n')
        print("Text saved to txt file.")
    except Exception as e:
        print(f"Error: Failed to save text to txt file: {e}")

# Function to copy text to clipboard
def copy_text_to_clipboard(text):
    """
    Copy the given text to the clipboard.

    Parameters:
    text (str): The text to be copied to the clipboard.
    """
    try:
        print("Copying text to clipboard.")
        pyperclip.copy(text)
        print("Text copied to clipboard.")
    except Exception as e:
        print(f"Error: Failed to copy text to clipboard: {e}")

# Main function to orchestrate the process
def main():
    """
    A function that represents the main execution flow. 
    It installs dependencies on the first run, 
    captures a screenshot, 
    converts the image to text, 
    saves the text to an RTF file, 
    copies the text to the clipboard, 
    and prints a message indicating that the text has been saved and copied to the clipboard.
    """
    install_dependencies() # only on first run
    screenshot_path = capture_screenshot()
    text = image_to_text(screenshot_path)
    save_text_to_rtf(text)
    copy_text_to_clipboard(text)
    print("Text has been saved and copied to clipboard.")

# Start the script
if __name__ == "__main__":
    main()