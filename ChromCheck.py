#Script for HB
import pyautogui
import pytesseract
from PIL import Image
import time
from datetime import datetime
import os
import re 

# Configure the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'  # Update with your Tesseract path

shared_drive_path = r"O:\Shares\Proteomics-Core-Lab-Data\ChromCheck"  # Update with your shared drive path

def log_error():
    error_file = os.path.join(shared_drive_path, f"error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(error_file, 'w') as file:
        file.write("Error detected at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def detect_error():
    screenshot = pyautogui.screenshot()
    text = pytesseract.image_to_string(screenshot)
    if "error" in text.lower():  
        return True
    
    pressure_pattern = r"Pressure: 290\.\d+"  # Pressure values set at 290.0
    if re.search(pressure_pattern, text):
        
        return False

def main():
    while True:
        if detect_error():
            log_error()
        time.sleep(60)  # 60 seconds interval between checks

if __name__ == "__main__":
    main()
