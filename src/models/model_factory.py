from .base_model import BaseModel
from .local_model import LocalModel
from .cloud_model import CloudModel

class ModelFactory:
    @staticmethod
    def get_model(provider: str) -> BaseModel:
        """
        Factory method to get the appropriate model implementation
        
        Args:
            provider: String indicating which model provider to use ('local' or 'cloud')
            
        Returns:
            An instance of the appropriate model class
        """
        if provider.lower() == "local":
            return LocalModel()
        elif provider.lower() == "cloud":
            return CloudModel()
        else:
            raise ValueError(f"Unknown model provider: {provider}") 