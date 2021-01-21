#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMainWindow, QLabel)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Example(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.statusBar().showMessage('Состояние')

        btn = QPushButton('выход', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(10, 10)

        lbl1 = QLabel('label1', self)
        lbl1.move(10, 40)

        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle('test5')
        self.setWindowIcon(QIcon('bit.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())