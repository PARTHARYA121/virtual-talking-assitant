
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout, QFrame, QLabel
from chatbot_engine import ChatbotEngine
from display_screen import DisplayScreen


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("chintu Chat")


        self.setStyleSheet("background-color: purple;")


        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QGridLayout(self.main_widget)

        
        self.browser1 = QFrame()
        self.browser2 = QFrame()
        self.ai_avatar = QFrame()
        self.transcript = QFrame()

        
        self.browser1.setStyleSheet("background-color: #333; border: 2px solid purple;")
        self.browser2.setStyleSheet("background-color: #333; border: 2px solid purple;")
        self.ai_avatar.setStyleSheet("background-color: #666; border: 2px solid purple;")
        self.transcript.setStyleSheet("background-color: #999; border: 2px solid purple;")

        
        self.main_layout.addWidget(self.browser1, 0, 0, 2, 3)
        self.main_layout.addWidget(self.browser2, 2, 0, 2, 3)
        self.main_layout.addWidget(self.ai_avatar, 0, 3, 2, 1)
        self.main_layout.addWidget(self.transcript, 2, 3, 2, 1)

      
        self.main_widget.setLayout(self.main_layout)

        
        image_label = QLabel()

        
        pixmap = QPixmap('assets/graphics/aidan interactive ai avatar.png')

        
        image_label.setPixmap(pixmap)

        
        ai_avatar_layout = QVBoxLayout()
        ai_avatar_layout.addWidget(image_label)
        self.ai_avatar.setLayout(ai_avatar_layout)


class MainApp(MainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot_engine = ChatbotEngine()
        self.display_screen = DisplayScreen()

       
        self.call_button = QPushButton("Call")
        self.pause_button = QPushButton("Pause")
        self.end_call_button = QPushButton("End Call")

        
        self.call_button.clicked.connect(self.on_call_button_clicked)
        self.pause_button.clicked.connect(self.chatbot_engine.stop)
        self.end_call_button.clicked.connect(self.chatbot_engine.stop)

       
        self.chatbot_engine.text_generated.connect(self.display_screen.display_text)

        layout = QVBoxLayout()
        layout.addWidget(self.display_screen)
        layout.addWidget(self.call_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.end_call_button)

        
        self.transcript.setLayout(layout)

        
        self.display_screen.display_text("", " Hello, My name is chintu. How can I help you? Go ahead. I'm listening.")

    def on_call_button_clicked(self):
        self.chatbot_engine.start()
        self.display_screen.display_text("", " The call has started. How can I assist you today?")


if __name__ == "__main__":
    app = QApplication([])
    main_app = MainApp()
    main_app.show()
    app.exec_()
