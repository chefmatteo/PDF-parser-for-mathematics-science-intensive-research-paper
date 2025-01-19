<<<<<<< HEAD
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
=======
from pathlib import Path
import pdfplumber
from ..utils.markdown_formatter import MarkdownFormatter
from ..utils.ocr_utils import OCRProcessor

class TextExtractor:
    def __init__(self):
        self.markdown_formatter = MarkdownFormatter()
        self.ocr_processor = OCRProcessor()
    
    def extract(self, pdf_path: Path) -> str:
        """Extract text content from PDF"""
        markdown_content = []
        
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if not text.strip():  # If page is scanned/image-based
                    text = self.ocr_processor.process_page(page)
                formatted_text = self.markdown_formatter.format(text)
                markdown_content.append(formatted_text)
                
        return "\n".join(markdown_content) 
>>>>>>> f665fe7831d9f6a00ff414ebfa44a17094d73c8d
