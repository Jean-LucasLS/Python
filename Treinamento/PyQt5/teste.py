import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        
        self.btn = QPushButton('Button text')
        self.btn.setStyleSheet('font-size: 10px;')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        self.setCentralWidget(self.cw)
        self.btn.clicked.connect(lambda: print('Olá!'))
if __name__ ==  '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()