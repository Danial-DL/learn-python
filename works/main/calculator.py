# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("/home/danial/project/python_projects/class_work/session_19/main/form.ui")
        self.ui.PB1.clicked.connect(self.addition)
        self.ui.PB2.clicked.connect(self.minus)
        self.ui.PB3.clicked.connect(self.cross)
        self.ui.PB4.clicked.connect(self.division)
        self.ui.PB5.clicked.connect(self.mumber_1)
        self.ui.PB6.clicked.connect(self.number_2)
        
        self.ui.show()
    def outpot(self):
        # a = 4 
        # b = 5
        # self.ui.textEdit.setText(str(result))
        self.out1 = self.a
        self.out2 = self.b
        #self.
    def addition(self):
        # D = 10
        # H = 4
        # result = D - H
        plus = "+"
        self.a = self.ui.textEdit.setText(plus)
        # self.ui.PB1.setText(self.ui.PB1.text()+"4")
    def minus(self):
        Minus = "-"
        self.ui.textEdit.setText(Minus)
    def cross(self):
        multiplication = "*"
        self.ui.textEdit.setText(multiplication)
    def division(self):
        divided = "/"
        self.ui.textEdit.setText(divided)
    def numbers(self):
        ...
    def mumber_1(self):
        one = "1"
        self.b = self.ui.textEdit.setText(one)
    def number_2(self):
        two = "2"
        self.c = self.ui.textEdit.setText(two)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
