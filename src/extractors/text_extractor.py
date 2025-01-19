import pdfplumber
from pathlib import Path
from src.utils.markdown_formatter import MarkdownFormatter
from src.utils.ocr_utils import OCRProcessor

class TextExtractor:
    """Class to handle text extraction from PDF documents"""
    
    def __init__(self):
        self.formatter = MarkdownFormatter()
        self.ocr_processor = OCRProcessor()
    
    def extract(self, pdf_path: str) -> str:
        """
        Extract text from PDF document
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            Extracted and formatted text
        """
        extracted_text = []
        
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extracted_text.append(text)
        
        # Join all text and format
        full_text = '\n\n'.join(extracted_text)
        return self.formatter.format(full_text) 