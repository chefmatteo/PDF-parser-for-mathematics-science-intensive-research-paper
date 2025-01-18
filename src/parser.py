from typing import List, Optional
from pathlib import Path
from .models.model_factory import ModelFactory
from .extractors.text_extractor import TextExtractor
from .extractors.image_extractor import ImageExtractor
from .extractors.latex_extractor import LatexExtractor

class PDFParser:
    def __init__(self, model_provider: str = "local"):
        self.model = ModelFactory.get_model(model_provider)
        self.text_extractor = TextExtractor()
        self.image_extractor = ImageExtractor()
        self.latex_extractor = LatexExtractor()
    
    def process_pdf(self, pdf_path: Path, output_dir: Path) -> dict:
        """Process PDF and return extracted content"""
        result = {
            "text": self.text_extractor.extract(pdf_path),
            "images": self.image_extractor.extract(pdf_path, output_dir),
            "equations": self.latex_extractor.extract(pdf_path)
        }
        return result 