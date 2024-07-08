class BMI:
	def __init__(self):
		self.Height = float(input("Please enter your height Meter (Please enter with decimals(.)):"))
		#User weight
		self.Weight = float(input("Enter your weight kg (Please enter with decimals(.)) : "))
		self.output = self.Weight/self.Height**2
	def man(self):
		if self.output >= 24.9 :
		    print("Warning! :/ Your BMI is higher than normal and indicates obesity and high risk of diabetes!!")
		    print("Our advice to you is: see a doctor and exercise daily, burn calories and eat healthy food, take anti-diabetic pills. :)")
		elif self.output <= 18.5 :
			print("Warning! /: Your BMI is lower than normal and indicates thinness and causes problems such as intestinal and stomach problems, vitamin deficiency,osteoporosis, malnutrition and muscle weakness.")
			print("Our advice to you is to see a doctor, change your eating habits and do proper exercise, use obesity drugs as prescribed by your doctor.")
		else:
			print("Your BMI is normal and you have a healthy body :)")
			print("have a nice day :)")
	def women(self):
		if self.output >= 23.9 :
			print("Warning! :/ Your BMI is higher than normal and indicates obesity and high risk of diabetes!!")
			print("Our advice to you is: see a doctor and exercise daily, burn calories and eat healthy food, take anti-diabetic pills. :)")
		elif self.output <= 17.5 :
			print("Warning! /: Your BMI is lower than normal and indicates thinness and causes problems such as intestinal and stomach problems, vitamin deficiency,osteoporosis, malnutrition and muscle weakness.")
			print("Our advice to you is to see a doctor, change your eating habits and do proper exercise, use obesity drugs as prescribed by your doctor.")
		else :
			print("Your BMI is normal and you have a healthy body :)")
			print("have a nice day :)")

gender = input("Please enter your gender (for example: MR or MS) : ")
bmi = BMI()
if gender == "MR":
	bmi.man()
elif gender == "MS":
	bmi.women()
else :
	print("Please enter your gender rithly")