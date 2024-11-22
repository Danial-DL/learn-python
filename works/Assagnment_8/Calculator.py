# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
import os

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        loader = QUiLoader()
        #self.Path = sys.executable
        self.Path = os.path.abspath(sys.argv[0])
        self.Path = self.Path[:-13]
        #print(self.Path)
        try :
            #self.Path = os.path.abspath(sys.argv[0])
            #print(self.Path )
            self.ui = loader.load(f"{self.Path}/form.ui")
        except :
            print(self.Path)
            print("Please put the form.ui file in the current path of the program!!")
        # Connect buttons to their functions
        self.ui.PB1.clicked.connect(self.addition)
        self.ui.PB2.clicked.connect(self.minus)
        self.ui.PB3.clicked.connect(self.cross)
        self.ui.PB4.clicked.connect(self.division)
        self.ui.PB5.clicked.connect(self.number_0)
        self.ui.PB6.clicked.connect(self.number_1)
        self.ui.PB7.clicked.connect(self.number_2)
        self.ui.PB8.clicked.connect(self.number_3)
        self.ui.PB9.clicked.connect(self.number_4)
        self.ui.PB10.clicked.connect(self.number_5)
        self.ui.PB11.clicked.connect(self.number_6)
        self.ui.PB12.clicked.connect(self.number_7)
        self.ui.PB13.clicked.connect(self.number_8)
        self.ui.PB14.clicked.connect(self.number_9)
        self.ui.PB15.clicked.connect(self.DELET)
        self.ui.PB16.clicked.connect(self.RESET)
        self.ui.PB17.clicked.connect(self.outpot)
        self.current_input = ""  # Variable to keep track of the current input
        
        self.ui.show()

    def update_display(self, value):
        try :
            self.current_input += value  # Append new value to the current input
            self.ui.textEdit.setText(self.current_input)  # Update the display
            def is_valid_expression(expr):
                return all(c.isdigit() or c == "+" for c in expr)
            #print(is_valid_expression(self.current_input))
            if is_valid_expression(self.current_input) == True and "+" in self.current_input or "-" in self.current_input or "*" in self.current_input or "/" in self.current_input:
                self.out = self.current_input  # Output to terminal
        except :
            self.ui.textEdit.setText("ERROR")
            self.current_input = ""
            self.ui.textEdit.setText(self.current_input)
    def outpot(self):
        try :
            self.result = eval(self.out)
            #print(self.out)
            self.ui.textEdit.setText(str(self.result))
            self.current_input = ""
        except :
            self.ui.textEdit.setText("ERROR!!")
            #time.sleep(5)
            self.current_input = ""
            # self.ui.textEdit.setText(self.current_input)
    def RESET(self):
        self.current_input = ""
        self.ui.textEdit.setText(self.current_input)

    def DELET(self):
        if self.current_input != "":
            self.current_input = self.current_input[:-1]
            self.ui.textEdit.setText(self.current_input)
        else :
            self.ui.textEdit.setText(self.current_input)
    def addition(self):
        self.update_display("+")
    
    def minus(self):
        self.update_display("-")
    
    def cross(self):
        self.update_display("*")
    
    def division(self):
        self.update_display("/")

    def number_0(self):
        self.update_display("0")

    def number_1(self):
        self.update_display("1")

    def number_2(self):
        self.update_display("2")

    def number_3(self):
        self.update_display("3")

    def number_4(self):
        self.update_display("4")

    def number_5(self):
        self.update_display("5")

    def number_6(self):
        self.update_display("6")

    def number_7(self):
        self.update_display("7")

    def number_8(self):
        self.update_display("8")

    def number_9(self):
        self.update_display("9")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())