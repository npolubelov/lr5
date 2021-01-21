#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        btn = QPushButton('кнопка1', self)
        btn.resize(btn.sizeHint())
        btn.move(10, 10)

        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle('test3')
        self.setWindowIcon(QIcon('bit.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())