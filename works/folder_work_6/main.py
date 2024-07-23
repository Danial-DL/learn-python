from work_6 import Date
while True :
    year_input = abs(int(input("Enter the year : ")))
    month_input = abs(int(input("Enter the month : ")))
    day_input = abs(int(input("Enter the day : ")))
    date = Date(day_input , month_input , year_input)
    while True :
        Selection = input("Select (add , get Month Name , Leap Year , minus , is Valid Date , ageDetection , show , exit) : ")
        if Selection == "add" :
            Day_plus_input = abs(int(input("Enter the day to add : ")))
            Month_plus_input = abs(int(input("Enter the month to add : ")))
            Year_plus_input = abs(int(input("Enter the year to add : ")))
            date.add(Day_plus_input,Month_plus_input,Year_plus_input)
        elif Selection == "get Month Name" :
            choic = int(input("Enter the month number and we will show you the month itself : "))
            date.getMonthName(choic)
        elif Selection == "Leap Year" :
            leap = int(input("Enter the year to check if it is a leap year or not : "))
            date.isLeapYear(leap)
        elif Selection == "minus" :
            Day_minus_input = abs(int(input("Enter the day to minus : ")))
            Month_minus_input = abs(int(input("Enter the month to minus : ")))
            Year_minus_input = abs(int(input("Enter the year to minus : ")))
            date.sub(Day_minus_input,Month_minus_input,Year_minus_input)
        elif Selection == "is Valid Date" :
            date.isValidDate()
        elif Selection == "ageDetection": 
            YEAR_birth = int(input("Enter your year of birth : "))
            MONTH_birth = int(input("Enter your birth month : "))
            DAY_birth = int(input("Enter your birthday : "))
            if not 0 > YEAR_birth > 9999 or 0 > MONTH_birth > 12 or 0 > DAY_birth > 30 :
                Date.ageDetection(YEAR_birth , MONTH_birth , DAY_birth)
            else :
                print("Inappropriate amount !!")
        elif Selection == "show" :
            date.Show()
        elif Selection == "exit" :
            break
        else :
            print("Not Found !!")

