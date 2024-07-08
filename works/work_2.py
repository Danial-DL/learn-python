class Calculator:
    def __init__(self):
        self.num1 = int(input("Enter number one : "))
        self.num2 = int(input("Enter number two : "))
    def plus(self):
        self.Answer1 = self.num1 + self.num2
        print(f"{self.num1} + {self.num2} = {self.Answer1}")
    def minus(self):
        self.Answer2 = self.num1 - self.num2
        print(f"{self.num1} - {self.num2} = {self.Answer2}")
    def multiplied(self):
        self.Answer3 = self.num1 * self.num2
        print(f"{self.num1} * {self.num2} = {self.Answer3}")
    def divided(self):
        self.Answer4 = self.num1 / self.num2
        print(f"{self.num1} / {self.num2} = {self.Answer4}")
while True :
    Calculation_type = input("Enter the desired calculation type (+,-,*,/) : ")
    Computing = calculator()
    if Calculation_type == "+":
        Computing.plus()
    elif Calculation_type == "-":
        Computing.minus()
    elif Calculation_type == "*":
        Computing.multiplied()
    elif Calculation_type == "/":
        Computing.divided()
    else :
        print("Please enter correctly ...")
