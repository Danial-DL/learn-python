import sqlite3

connectMarket = sqlite3.connect("SuperMarket.db")

MyConnect = connectMarket.cursor()


class Market:
    def __init__(self , name , Table , lable , amount , enter1 , enter2 , enter3 , enter4 , enter5 , select_Table):
        self.name = name
        self.Table = Table
        self.lable = lable
        self.amount = amount
        self.enter1 = enter1
        self.enter2 = enter2
        self.enter3 = enter3
        self.enter4 = enter4
        self.enter5 = enter5
        self.select_Table = select_Table
        

    def show(self):
        print(f"{self.name} : ")
        for data in MyConnect.execute(f"SELECT * FROM {self.name}"):
            print(data)        

    def find(self):
        if self.amount == "number" :
            num = input("Enter number : ")
            result = MyConnect.execute(f"SELECT * FROM {self.Table} WHERE {self.lable}={num}")
        elif self.amount == "string" :
            string = input("Enter string : ")
            result = MyConnect.execute(f"SELECT * FROM {self.Table} WHERE {self.lable}='{string}'") 
        else :
            print("Error") 

        info = result.fetchall()
        print(info)

    def add(self):
        MyConnect.execute(f"INSERT INTO {self.select_Table}(id,name,weight,sum,price) values({self.enter1} , '{self.enter2}' , {self.enter3} , {self.enter4} , {self.enter5})")
        connectMarket.commit()





if __name__ == "__main__":
    
    name = input("enter Name : ")

    Table = input("Enter Table : ")

    lable = input("enter lable : ")
    amount = input("enter number or string : ")


    enter1 = input("enter id : ")
    enter2 = input("enter name : ")
    enter3 = input("enter weight : ")
    enter4 = input("enter sum : ")
    enter5 = input("enter price : ")

    Table_select = input("Enter Table : ")

    myMarket = Market(name , Table , lable , amount , enter1 , enter2 , enter3 , enter4 , enter5 , Table_select)

    select = input("What do you plan to do with the database? show , find , add :")

    if select == "show" :
        myMarket.show()
    elif select == "find" :
        myMarket.find()
    elif select == "add" :
        myMarket.add()
    else :
        print("Error Not found")


