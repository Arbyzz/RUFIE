from PyQt5.QtCore import Qt
from window4 import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
class MainWin(QWidget):
    def __init__(self):
        supper().__init__()
        self.set_apper()
        self.initUI()
        self.connects()
        self.show()
        def set_apper(self):
            self.setWindowTitle(txt_title)
            self.resize(win_width, win_height)
            self.move(win_x, win_y)
        def initUI(self):
            pass
        def connects(sef):
            pass
        