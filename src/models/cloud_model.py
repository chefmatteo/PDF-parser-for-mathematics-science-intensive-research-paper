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
        raise NotImplementedError("Cloud model not yet implemented") 