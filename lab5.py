#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QTextEdit, QLCDNumber, QSlider)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt

class Example(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.statusBar().showMessage('Состояние')
        
        btn1 = QPushButton('выход', self)
        btn1.clicked.connect(QCoreApplication.instance().quit)
        btn1.move(50, 10)

        btn2 = QPushButton('выход2', self)
        btn2.clicked.connect(QCoreApplication.instance().quit)
        btn2.move(200, 10)

        btn3 = QPushButton('выход3', self)
        btn3.clicked.connect(QCoreApplication.instance().quit)
        btn3.move(350, 10)
            
        lbl1 = QLabel('label1', self)
        lbl1.move(50, 50)

        lcd = QLCDNumber(self)
        lcd.move(50, 100)
        sld = QSlider(Qt.Horizontal, self)
        sld.move(50, 150)
     
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(0, 0, 500, 300)
        self.setWindowTitle('test6')
        self.setWindowIcon(QIcon('bit.png'))
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())