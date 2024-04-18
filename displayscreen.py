
from PyQt5.QtWidgets import QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class DisplayScreen(QWidget):
    def __init__(self, parent=None):
        super(DisplayScreen, self).__init__(parent)
        self.transcript = QTextEdit()
        self.transcript.setStyleSheet(
            "background-color: #333; color: white;") 
        self.transcript.setReadOnly(True)

        
        self.browser = QWebEngineView()

        
        layout = QVBoxLayout()
        layout.addWidget(self.transcript)
        layout.addWidget(self.browser)
        self.setLayout(layout)

    def display_text(self, recognized_text, generated_text):
        
        self.transcript.append(f"You: {recognized_text}\nchintu: {generated_text}")

    
        if "http://" in generated_text or "https://" in generated_text:
    
            url = generated_text.split()[-1]  

        
            self.browser.load(QUrl(url))
