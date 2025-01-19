import re

class MarkdownFormatter:
    """Utility class to format extracted content into Markdown"""
    
    @staticmethod
    def format(text: str) -> str:
        """
        Format raw text into markdown format
        
        Args:
            text: Raw text to format
            
        Returns:
            Formatted markdown text
        """
        return MarkdownFormatter.format_text(text)
    
    @staticmethod
    def format_text(text: str) -> str:
        """Format extracted text into markdown paragraphs"""
        # Split text into paragraphs and clean up
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        
        # Format each paragraph
        formatted_paragraphs = []
        for p in paragraphs:
            # Remove excess whitespace within paragraph while preserving single spaces
            p = ' '.join(p.split())
            # Add paragraph to list
            formatted_paragraphs.append(p)
            
        # Join paragraphs with double newlines and add extra spacing
        formatted_text = '\n\n'.join(formatted_paragraphs)
        
        # Add extra spacing for visual separation in QTextEdit
        formatted_text = formatted_text.replace('\n\n', '\n\n\n')
        
        return formatted_text
    
    @staticmethod
    def format_equation(equation: str) -> str:
        """Format LaTeX equation into markdown math block"""
        return f"$$\n{equation}\n$$"
    
    @staticmethod
    def format_image(image_path: str, caption: str = "") -> str:
        """Format image reference into markdown"""
        if caption:
            return f"![{caption}]({image_path})"
        return f"![]({image_path})"
    
    @staticmethod
    def combine_content(text_blocks: list, equations: list, images: list) -> str:
        """Combine different content types into a single markdown document"""
        markdown = []
        
        # Add text blocks with proper spacing
        for block in text_blocks:
            markdown.append(MarkdownFormatter.format_text(block))
        
        # Add equations if present
        if equations:
            markdown.append("\n\n### Equations\n")
            for eq in equations:
                markdown.append(MarkdownFormatter.format_equation(eq))
        
        # Add images if present
        if images:
            markdown.append("\n\n### Images\n")
            for img_path in images:
                markdown.append(MarkdownFormatter.format_image(img_path))
        
        # Join all content with extra spacing
        return "\n\n\n".join(markdown) 