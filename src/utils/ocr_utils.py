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
        return pytesseract.image_to_string(img, config=self.config) 