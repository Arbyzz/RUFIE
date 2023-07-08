from PyQt5.QtCore import Qt
from window4 import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apper()
        self.initUI()
        self.show()
    def set_apper(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.end = QLabel(final_text)
        self.end_heart = QLabel(heart)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.end, alignment= Qt.AlignCenter)
        self.layout.addWidget(self.end_heart, alignment= Qt.AlignCenter)
        self.setLayout(self.layout)
