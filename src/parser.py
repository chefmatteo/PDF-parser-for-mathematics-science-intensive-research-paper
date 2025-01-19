from typing import List, Optional
from pathlib import Path
from src.models.model_factory import ModelFactory
from src.extractors.text_extractor import TextExtractor
from src.extractors.image_extractor import ImageExtractor
from src.extractors.latex_extractor import LatexExtractor
from src.extractors.citation_extractor import CitationExtractor

class PDFParser:
    def __init__(self, model_provider: str = "local"):
        self.model = ModelFactory.get_model(model_provider)
        self.text_extractor = TextExtractor()
        self.image_extractor = ImageExtractor()
        self.latex_extractor = LatexExtractor()
        self.citation_extractor = CitationExtractor()
    
    def process_pdf(self, pdf_path: Path, output_dir: Path) -> dict:
        """Process PDF and return extracted content"""
        result = {
            "text": self.text_extractor.extract(pdf_path),
            "images": self.image_extractor.extract(pdf_path, output_dir),
            "equations": self.latex_extractor.extract(pdf_path),
            "citations": self.citation_extractor.extract(pdf_path)
        }
        return result 