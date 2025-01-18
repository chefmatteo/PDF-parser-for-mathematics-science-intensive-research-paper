import fitz  # PyMuPDF
import cv2
import numpy as np
from pathlib import Path
import os 

class ImageExtractor:
    """Class to handle image extraction from PDF documents"""
    
    def __init__(self):
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.bmp'] # Supported image formats
    
    def extract(self, pdf_path: str, output_dir: Path) -> list: 
        """
        Extract images from PDF and save them to output directory
        
        Args:
            pdf_path: Path to PDF file
            output_dir: Directory to save extracted images
            
        Returns:
            List of paths to extracted images
        """
        return self.extract_images(pdf_path, output_dir)
    
    def extract_images(self, pdf_path: str, output_dir: Path) -> list:
        """
        Extract images from PDF and save them to output directory
        
        Args:
            pdf_path: Path to PDF file
            output_dir: Directory to save extracted images
            
        Returns:
            List of paths to extracted images
        """
        # Create images subdirectory
        images_dir = output_dir / "images"
        images_dir.mkdir(exist_ok=True)
        
        doc = fitz.open(pdf_path)
        image_paths = []
        
        # Iterate through pages
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # Get images from page
            image_list = page.get_images(full=True)
            
            # Process each image
            for img_idx, img_info in enumerate(image_list):
                img_idx_str = str(img_idx + 1).zfill(3)
                xref = img_info[0]
                base_image = doc.extract_image(xref)
                
                if base_image:
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    
                    # Only save supported image formats
                    if f'.{image_ext.lower()}' in self.supported_formats:
                        # Create image filename
                        image_name = f"page_{page_num + 1}_img_{img_idx_str}.{image_ext}"
                        image_path = images_dir / image_name
                        
                        # Save image
                        with open(image_path, "wb") as img_file:
                            img_file.write(image_bytes)
                        
                        # Add to list of image paths
                        image_paths.append(str(image_path.relative_to(output_dir)))
        
        doc.close()
        return image_paths
    
    def _enhance_image(self, image_bytes: bytes) -> bytes:
        """
        Enhance image quality if needed
        
        Args:
            image_bytes: Raw image bytes
            
        Returns:
            Enhanced image bytes
        """
        # Convert bytes to numpy array
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            return image_bytes
            
        # Basic enhancement
        img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
        
        # Convert back to bytes
        success, enhanced_img = cv2.imencode('.png', img)
        if success:
            return enhanced_img.tobytes()
        return image_bytes 