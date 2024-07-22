from datetime import date
from random import choice , randrange
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
while True:
    YEAR_birth = int(input("Enter your year of birth : "))
    MONTH_birth = int(input("Enter your birth month : "))
    DAY_birth = int(input("Enter your birthday : "))
    if not 0 > YEAR_birth > 9999 or 0 > MONTH_birth > 12 or 0 > DAY_birth > 30 :
        ageDetection(YEAR_birth , MONTH_birth , DAY_birth)
    else :
        print("Not found !!")