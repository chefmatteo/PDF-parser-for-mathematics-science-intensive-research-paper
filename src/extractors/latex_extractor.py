import re
import cv2
import numpy as np
from pathlib import Path
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
import logging

class LatexExtractor:
    """Class to handle LaTeX equation extraction from PDF documents"""
    
    def __init__(self):
        self.equation_patterns = [
            r'\$\$(.*?)\$\$',  # Display math mode
            r'\$(.*?)\$',      # Inline math mode
            r'\\begin{equation}(.*?)\\end{equation}',
            r'\\begin{align}(.*?)\\end{align}',
            r'\\begin{gather}(.*?)\\end{gather}'
        ]
        self.tesseract_available = self._check_tesseract()
        
    def _check_tesseract(self) -> bool:
        """Check if Tesseract OCR is available"""
        try:
            pytesseract.get_tesseract_version()
            return True
        except pytesseract.TesseractNotFoundError:
            logging.warning("Tesseract OCR not found. Image-based equation extraction will be disabled.")
            return False
    
    def extract(self, pdf_path: str) -> list:
        """
        Extract equations from PDF document
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            List of extracted LaTeX equations
        """
        equations = []
        
        # Open PDF
        doc = fitz.open(pdf_path)
        
        # Extract text from each page
        for page in doc:
            text = page.get_text()
            equations.extend(self.extract_equations(text))
            
            # Only attempt image-based extraction if Tesseract is available
            if self.tesseract_available:
                # Also check images for equations
                image_list = page.get_images(full=True)
                for img_info in image_list:
                    xref = img_info[0]
                    base_image = doc.extract_image(xref)
                    if base_image:
                        # Create temporary image file
                        temp_path = Path("temp_image.png")
                        try:
                            with open(temp_path, "wb") as f:
                                f.write(base_image["image"])
                            
                            # Extract equations from image
                            img_equations = self.extract_equations_from_image(str(temp_path))
                            equations.extend(img_equations)
                        except Exception as e:
                            logging.error(f"Error processing image: {e}")
                        finally:
                            # Clean up temp file
                            if temp_path.exists():
                                temp_path.unlink()
        
        doc.close()
        return list(set(equations))  # Remove duplicates
    
    def extract_equations(self, text: str) -> list:
        """Extract LaTeX equations from text"""
        equations = []
        
        # Search for equations using patterns
        for pattern in self.equation_patterns:
            matches = re.finditer(pattern, text, re.DOTALL)
            for match in matches:
                equation = match.group(1).strip()
                if equation and self._is_valid_equation(equation):
                    equations.append(equation)
        
        return equations
    
    def extract_equations_from_image(self, image_path: str) -> list:
        """Extract equations from images using OCR"""
        if not self.tesseract_available:
            return []
            
        try:
            # Load and preprocess image
            img = cv2.imread(image_path)
            if img is None:
                return []
                
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Basic image preprocessing
            gray = cv2.GaussianBlur(gray, (3, 3), 0)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
            
            # OCR with special configuration for math
            custom_config = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(thresh, config=custom_config)
            
            # Extract equations from OCR text
            return self.extract_equations(text)
        except Exception as e:
            logging.error(f"Error in OCR processing: {e}")
            return []
    
    def _is_valid_equation(self, equation: str) -> bool:
        """Basic validation of LaTeX equation"""
        math_indicators = [
            '\\frac', '\\sum', '\\int', '\\alpha', '\\beta',
            '\\theta', '\\pi', '\\infty', '\\partial', '\\nabla',
            '+', '-', '=', '\\times', '\\div'
        ]
        return any(indicator in equation for indicator in math_indicators) 