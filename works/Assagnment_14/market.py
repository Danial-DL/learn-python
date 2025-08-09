import sqlite3

connectMarket = sqlite3.connect("SuperMarket.db")

MyConnect = connectMarket.cursor()

print("drink : ")
for data in MyConnect.execute("SELECT * FROM drink"):
    print(data)

print("snacks : ")
for data in MyConnect.execute("SELECT * FROM snacks"):
    print(data)

print("CannedFoods : ")
for data in MyConnect.execute("SELECT * FROM CannedFoods"):
    print(data)

print("Detergent : ")
for data in MyConnect.execute("SELECT * FROM Detergent"):
    print(data)

print("iceCream")
for data in MyConnect.execute("SELECT * FROM iceCream"):
    print(data)

print("legumes : ")
for data in MyConnect.execute("SELECT * FROM iceCream"):
    print(data)

Table = input("Enter Table : ")

lable = input("enter lable : ")
amount = input("enter number or string : ")
if amount == "number" :
    num = input("Enter number : ")
    result = MyConnect.execute(f"SELECT * FROM {Table} WHERE {lable}={num}")
elif amount == "string" :
    string = input("Enter string : ")
    result = MyConnect.execute(f"SELECT * FROM {Table} WHERE {lable}='{string}'") 
else :
    print("Error")  

info = result.fetchall()
print(info)

enter1 = input("enter id : ")
enter2 = input("enter name : ")
enter3 = input("enter weight : ")
enter4 = input("enter sum : ")
enter5 = input("enter price : ")

Table = input("Enter Table : ")
MyConnect.execute(f"INSERT INTO {Table}(id,name,weight,sum,price) values({enter1} , '{enter2}' , {enter3} , {enter4} , {enter5})")
connectMarket.commit()
