<<<<<<< HEAD
import pytesseract
from PIL import Image
import numpy as np

class OCRProcessor:
    def __init__(self):
        self.config = '--psm 3'  # Page segmentation mode
        
    def process_page(self, page) -> str:
        """Process a page using OCR"""
        # Convert page to image
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Perform OCR
=======
import pytesseract
from PIL import Image
import numpy as np

class OCRProcessor:
    def __init__(self):
        self.config = '--psm 3'  # Page segmentation mode
        
    def process_page(self, page) -> str:
        """Process a page using OCR"""
        # Convert page to image
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Perform OCR
>>>>>>> f665fe7831d9f6a00ff414ebfa44a17094d73c8d
        return pytesseract.image_to_string(img, config=self.config) 