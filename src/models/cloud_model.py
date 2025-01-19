<<<<<<< HEAD
from .base_model import BaseModel

class CloudModel(BaseModel):
    def __init__(self):
        super().__init__()
        
    def load_model(self):
        """Load cloud-based model"""
        raise NotImplementedError("Cloud model not yet implemented")
        
    def extract_text(self, image):
        """Extract text using cloud API"""
        raise NotImplementedError("Cloud model not yet implemented")
        
    def extract_equations(self, image):
        """Extract equations using cloud API"""
=======
from .base_model import BaseModel

class CloudModel(BaseModel):
    def __init__(self):
        super().__init__()
        
    def load_model(self):
        """Load cloud-based model"""
        raise NotImplementedError("Cloud model not yet implemented")
        
    def extract_text(self, image):
        """Extract text using cloud API"""
        raise NotImplementedError("Cloud model not yet implemented")
        
    def extract_equations(self, image):
        """Extract equations using cloud API"""
>>>>>>> f665fe7831d9f6a00ff414ebfa44a17094d73c8d
        raise NotImplementedError("Cloud model not yet implemented") 