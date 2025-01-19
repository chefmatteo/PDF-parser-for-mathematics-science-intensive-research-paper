<<<<<<< HEAD
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
=======
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
>>>>>>> f665fe7831d9f6a00ff414ebfa44a17094d73c8d
            raise ValueError(f"Unknown model provider: {provider}") 