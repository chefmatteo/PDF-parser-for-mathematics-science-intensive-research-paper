from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QPushButton, QTextEdit, QFileDialog, QLabel, QScrollArea,
                           QFrame)
from PyQt6.QtCore import Qt, QSize, QMimeData
from PyQt6.QtGui import QPixmap, QDragEnterEvent, QDropEvent
from pathlib import Path
from src.parser import PDFParser
from src.extractors.citation_extractor import CitationExtractor

class DropZone(QFrame):
    """Custom drop zone widget for PDF files"""
    
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Store reference to main window
        self.setAcceptDrops(True)
        self.setMinimumSize(200, 100)
        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Sunken)
        
        # Create layout
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add icon and text
        self.label = QLabel("Drop PDF here\nor click to browse")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                color: #666;
                font-size: 14px;
            }
        """)
        layout.addWidget(self.label)
        
        self.setStyleSheet("""
            DropZone {
                background-color: #f8f9fa;
                border: 2px dashed #ccc;
                border-radius: 10px;
            }
            DropZone:hover {
                background-color: #e9ecef;
                border-color: #4CAF50;
            }
        """)
        
    def dragEnterEvent(self, event: QDragEnterEvent):
        """Handle drag enter events"""
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            if url.toLocalFile().lower().endswith('.pdf'):
                event.acceptProposedAction()
    
    def dropEvent(self, event: QDropEvent):
        """Handle drop events"""
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.main_window.process_pdf(file_path)  # Use main_window reference
        
    def mousePressEvent(self, event):
        """Handle mouse click events"""
        self.main_window.open_file_dialog()  # Use main_window reference

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.parser = PDFParser(model_provider="local")
        self.citation_extractor = CitationExtractor()
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle('PDF Content Extractor')
        self.setMinimumSize(1200, 800)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Add drop zone at the top
        self.drop_zone = DropZone(self)  # Pass self as main_window
        layout.addWidget(self.drop_zone)
        
        # Create content area with three columns
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        
        # Create left panel for text content
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # Add text display area
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        self.text_display.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
        """)
        left_layout.addWidget(QLabel("Extracted Content"))
        left_layout.addWidget(self.text_display)
        
        # Create right panel for images
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Add scroll area for images
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: 1px solid #cccccc;
                border-radius: 5px;
                background-color: #f5f5f5;
            }
        """)
        
        self.image_container = QWidget()
        self.image_layout = QVBoxLayout(self.image_container)
        self.image_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll.setWidget(self.image_container)
        
        right_layout.addWidget(QLabel("Extracted Images"))
        right_layout.addWidget(scroll)
        
        # Add right panel for citations
        citations_panel = QWidget()
        citations_layout = QVBoxLayout(citations_panel)
        
        # Add citations display area
        self.citations_display = QTextEdit()
        self.citations_display.setReadOnly(True)
        self.citations_display.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                line-height: 1.4;
            }
        """)
        
        citations_layout.addWidget(QLabel("References"))
        citations_layout.addWidget(self.citations_display)
        
        # Add all panels to content layout
        content_layout.addWidget(left_panel, stretch=2)  # Text content
        content_layout.addWidget(right_panel, stretch=1)  # Images
        content_layout.addWidget(citations_panel, stretch=1)  # Citations
        
        layout.addWidget(content_widget)
        
    def open_file_dialog(self):
        """Open file dialog to select PDF"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select PDF File",
            "",
            "PDF Files (*.pdf)"
        )
        if file_path:
            self.process_pdf(file_path)
    
    def process_pdf(self, file_path: str):
        """Process the selected PDF file"""
        pdf_path = Path(file_path)
        output_dir = Path("extracted_content")
        output_dir.mkdir(exist_ok=True)
        
        # Update drop zone text
        self.drop_zone.label.setText(f"Processing: {pdf_path.name}")
        
        try:
            # Process PDF
            result = self.parser.process_pdf(pdf_path, output_dir)
            
            # Display text content with proper spacing
            self.text_display.setPlainText(result["text"])  # Use setPlainText instead of setText
            
            # Set a larger line spacing for the text display
            self.text_display.setStyleSheet("""
                QTextEdit {
                    background-color: #ffffff;
                    border: 1px solid #cccccc;
                    border-radius: 5px;
                    padding: 10px;
                    font-size: 14px;
                    line-height: 1.6;
                }
            """)
            
            # Clear previous images
            for i in reversed(range(self.image_layout.count())): 
                self.image_layout.itemAt(i).widget().setParent(None)
            
            # Display images
            for img_path in result["images"]:
                full_path = output_dir / img_path
                if full_path.exists():
                    # Create image label
                    img_label = QLabel()
                    pixmap = QPixmap(str(full_path))
                    scaled_pixmap = pixmap.scaled(
                        QSize(300, 300), 
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                    img_label.setPixmap(scaled_pixmap)
                    img_label.setStyleSheet("""
                        QLabel {
                            background-color: white;
                            border: 1px solid #cccccc;
                            border-radius: 5px;
                            padding: 5px;
                            margin: 5px;
                        }
                    """)
                    self.image_layout.addWidget(img_label)
            
            # Extract and display citations
            citations = self.citation_extractor.extract(file_path)
            if citations:
                citations_text = []
                for i, citation in enumerate(citations, 1):
                    citations_text.append(f"[{i}] {citation}")
                self.citations_display.setPlainText('\n\n'.join(citations_text))
            else:
                self.citations_display.setPlainText("No references found")
            
            # Reset drop zone text
            self.drop_zone.label.setText("Drop PDF here\nor click to browse")
            
        except Exception as e:
            self.text_display.setText(f"Error processing PDF: {str(e)}")
            self.citations_display.setText("Error extracting citations")
            self.drop_zone.label.setText("Error! Try another file") 