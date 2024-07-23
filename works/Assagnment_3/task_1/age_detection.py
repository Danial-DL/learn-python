from datetime import date
from random import choice , randrange
# from random import randint
today = date.today()
print("Today's date:", today)
class Date :
    def __init__(self,Day=0,Month=0,Year=0):
        self.today = date.today()
        self.DATE = str(self.today)
        self.list_DATE = self.DATE.split("-")
        self.day = Day
        self.month = Month
        self.year = Year
    def add(self,DAY,MONTH,YEAR):
        Day_plus = self.day + DAY
        Month_plus = self.month + MONTH
        Year_plus = self.year + YEAR
        while Day_plus > 30 or Month_plus > 12 :
            if Day_plus > 30 :
                Day_plus -= 30 
                Month_plus += 1
            if Month_plus > 12 :
                Month_plus -= 12 
                Year_plus += 1
        print(f"Date Plus : {Year_plus}/{Month_plus}/{Day_plus}")
    def getMonthName(self,EntereMonth):
        Month = { 1 : "January" , 2 : "February" , 3 : "March" , 4 : "April" , 5 : "May" , 6 : "June" , 7 : "July" , 8 : "August" , 9 : "September" , 10 : "October" , 11 : "November" , 12 : "December" }
        if EntereMonth > 12 or EntereMonth <= 0:
            print("Not Fond")
        else :
            print(f"Month name : {Month[EntereMonth]}")
    def isLeapYear(self,Num_Year):
        if Num_Year % 4 == 0 :
            print(True) , print(f"Year {Num_Year} is a leap year ({True})")
        else :
            print(False) , print(f"Year {Num_Year} is not a leap year ({False})")
    def sub(self,DAY,MONTH,YEAR):
        Day_Minus = self.day - DAY
        Month_Minus = self.month - MONTH
        Year_Minus = self.year - YEAR
        while Day_Minus < 0 or Month_Minus < 0 :
            if Day_Minus < 0 :
                Day_Minus = 30 + Day_Minus
                Month_Minus -= 1
            if Month_Minus < 0 :
                Month_Minus = 12 + Month_Minus
                Year_Minus -= 1
        print(f"Date Plus : {Year_Minus}/{Month_Minus}/{Day_Minus}")  
    def isValidDate(self):
        if 0 >= self.day > 30 or 0 >= self.month > 12 or 0 >= self.year > 9999 :
            print(False) , print(f"No such date : {self.year}/{self.month}/{self.day} ({False})")
        else :
            print(True) , print(f"There is such a date : {self.year}/{self.month}/{self.day} ({True})")
    def ageDetection(YEAR_birth , Month_birth , Day_birth) :
        today = date.today()
        DATE = str(today)
        list_DATE = DATE.split("-")
        print("Today's date:", today)
        YEAR_age = int(list_DATE[0]) - YEAR_birth
        MONTH_age = int(list_DATE[1]) - Month_birth
        DAY_age = int(list_DATE[2]) - Day_birth
        if MONTH_age == 0 and DAY_age == 0 :
            print("Happy Birthday :)")
            a = ["✨" , "🎉" , "🎊" , "🎇" , "🎆" , "🎈" , "🧁" , "🍬" , "🍰" , "🍩"]            
            for i in range(10):
                print((choice(a) + "       " ) + (choice(a) + "       " ) + (choice(a) + "      " ) + (choice(a) + "      " ))
        print(f"Your age is => year : {YEAR_age} , mounth : {MONTH_age} , day : {DAY_age}")
    def Show(self):
        print(f"Today time : {self.list_DATE[0]}/{self.list_DATE[1]}/{self.list_DATE[2]}")
        print(f"Entry time : {self.year}/{self.month}/{self.day}")
