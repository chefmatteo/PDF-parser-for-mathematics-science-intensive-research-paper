from abc import ABC, abstractmethod

class BaseModel(ABC):
    """Base class for all OCR/text extraction models"""
    
    def __init__(self):
        self.model = None
        
    def load_model(self):
        """Load the model - to be implemented by child classes"""
        raise NotImplementedError
        
    def extract_text(self, image):
        """Extract text from image - to be implemented by child classes"""
        raise NotImplementedError
        
    def extract_equations(self, image):
        """Extract equations from image - to be implemented by child classes"""
        raise NotImplementedError 