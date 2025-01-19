<<<<<<< HEAD
from .base_model import BaseModel
import pytesseract
from PIL import Image

class LocalModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.load_model()
        
    def load_model(self):
        """Initialize Tesseract OCR"""
        # Tesseract is loaded on-demand, no explicit loading needed
        pass
        
    def extract_text(self, image):
        """Extract text from image using Tesseract OCR"""
        if isinstance(image, str):
            image = Image.open(image)
        text = pytesseract.image_to_string(image)
        return text
        
    def extract_equations(self, image):
        """Extract equations from image"""
        # Basic implementation - could be enhanced with equation detection
=======
from .base_model import BaseModel
import pytesseract
from PIL import Image

class LocalModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.load_model()
        
    def load_model(self):
        """Initialize Tesseract OCR"""
        # Tesseract is loaded on-demand, no explicit loading needed
        pass
        
    def extract_text(self, image):
        """Extract text from image using Tesseract OCR"""
        if isinstance(image, str):
            image = Image.open(image)
        text = pytesseract.image_to_string(image)
        return text
        
    def extract_equations(self, image):
        """Extract equations from image"""
        # Basic implementation - could be enhanced with equation detection
>>>>>>> f665fe7831d9f6a00ff414ebfa44a17094d73c8d
        return [] 