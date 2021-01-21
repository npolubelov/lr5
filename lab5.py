#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMainWindow, QLabel, QHBoxLayout, 
    QVBoxLayout, QLineEdit, QTextEdit, QLCDNumber, QSlider, 
    QInputDialog, QAction, QFileDialog)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt

class Example(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.statusBar()
        
        btn1 = QPushButton('кнопка1', self)
        btn1.clicked.connect(self.buttonClicked)
        btn1.move(50, 10)

        btn2 = QPushButton('кнопка2', self)
        btn2.clicked.connect(self.showDialog1)
        btn2.move(200, 10)

        btn3 = QPushButton('кннопка3', self)
        btn3.clicked.connect(self.showDialog)
        btn3.move(350, 10)
            
        lbl1 = QLabel('label1', self)
        lbl1.move(50, 50)
        self.le = QLineEdit(self)
        self.le.move(100, 50)

        lcd = QLCDNumber(self)
        lcd.move(50, 100)
        sld = QSlider(Qt.Horizontal, self)
        sld.move(50, 150)
     
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(0, 0, 500, 300)
        self.setWindowTitle('test6')
        self.setWindowIcon(QIcon('bit.png'))
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' была нажата')
    
    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Диалоговое окно','введите текст:')

        if ok:
            self.le.setText(str(text))
    
    def showDialog1(self):

        fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '/home')[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.le.setText(data)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())