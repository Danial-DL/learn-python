class Store:
    def __init__(self):
        self.id = None
        self.name = None
        self.price = None
        self.count = None
        self.product = []
        self.list_input = []
        self.product_search = []
        self.Previous_list = []
    def read_from_database(self):
        try :
            f = open("database_work_5.csv","r")
            big_text = f.read()
            self.product_list = big_text.split("\n")
            #print(product_list)
            for i in range(len(self.product_list)):
                info = self.product_list[i].split(",")
                #print(info)
                self.product.append({"id":info[0],"name":info[1],"price":info[2],"count" : info[3]})
            return self.product
            #print(self.product)
        except Exception as e :
            print(e)
            self.product= []
            return self.product
            print(self.product)
        #print(self.product)
    def add(self,id=0,name=0,price=0,count=0):
        try :
            self.product.clear()
            self.id = id
            self.name = name
            self.price = price
            self.count = count
            self.list_input.append(self.id)
            self.list_input.append(self.name)
            self.list_input.append(self.price)
            self.list_input.append(self.count)
            with open("database_work_5.csv","a") as file:
                for i in self.list_input:
                    a = ",".join(self.list_input)
                file.write("\n" + a )
                self.list_input.clear()
            #return self.product_list
        except Exception as e :
            print(e)
    def search(self):
        try :
            f = open("database_work_5.csv","r")
            big_text2 = f.read()
            self.product_list2 = big_text2.split("\n")
            #print(product_list)
            for i in range(len(self.product_list2)):
                info = self.product_list2[i].split(",")
                #print(info)
                self.product_search.append({"id":info[0],"name":info[1],"price":info[2],"count" : info[3]})
            #return self.product_search
            #print(self.product_search)
        except Exception as e :
            print(e)
            self.product_search = []
            #return self.product_search
            #print(self.product_search)
        self.line = len(self.product_search)
        self.Select_row = int(input(f"This database has {self.line} rows. Enter the desired row : "))
        if self.Select_row > self.line or 0 >= self.Select_row :
            print("not found")
        else :
            self.Select_search = input("To display the information, just enter the name of the desired information(id,name,price,count) : ")
            if self.Select_search == "id" or self.Select_search == "name" or self.Select_search == "price" or self.Select_search == "count" :
                print(self.product_search[self.Select_row - 1][self.Select_search])
                self.product_search.clear()
            else :
                print("not found key !!")
    def show_all(self):
        try :
            FILE = open("database_work_5.csv","r")
            print(FILE.read())
        except Exception as e :
            print(e)
    def remove(self):
        try :
            with open("database_work_5.csv","r") as File :
                line = File.readlines()
                num = len(line)
                trash_bin = int(input(f"This database has {num} rows, select the row you want to delete : "))
                if trash_bin > num or 0 >= trash_bin :
                    print("Not found")    
                else :
                    with open("database_work_5.csv","r") as File :
                        previous_state = File.read()
                        self.Previous_list = previous_state.split("\n")
                        #print(self.Previous_list)
                        del self.Previous_list[trash_bin - 1]
                        with open("database_work_5.csv","w") as File :
                            for i in range(len(self.Previous_list)-1):
                                File.write(self.Previous_list[i] + "\n") 
                            File.write(self.Previous_list[-1])
                            #print(self.Previous_list)
                            self.Previous_list.clear()
        except Exception as e:
            print(e)
            self.Previous_list.clear()
    def update(self):
        try :
            list_change = []
            li = []
            list2 = []
            with open("database_work_5.csv","r") as File :
                line = File.readlines()
                num = len(line)
                Changing = int(input(f"This database has {num} rows, Select a row to change : "))
                if Changing > num or 0 >= Changing :
                    print("Not found") 
                else :
                    change = input("What do you want to change in the row (id,name,price,count) :")
                    if change == "id" or change == "name" or change == "price" or change == "count" :
                        with open("database_work_5.csv","r") as File :
                            previous_state = File.read()
                            self.Previous_list = previous_state.split("\n")
                            with open("database_work_5.csv","w") as File :
                                for i in self.Previous_list:
                                    list_change = i.split(",")
                                    li.append(list_change)
                                #print(li)
                                list2 = li[Changing - 1]
                                #print(list2)
                                if change == "id" :
                                    New_id = input("Enter the desired new ID :")
                                    list2[0] = New_id
                                elif change == "name" :
                                    New_name = input("Enter the desired new name :")
                                    list2[1] = New_name
                                elif change == "price" :
                                    New_price = input("Enter the desired new price :")
                                    list2[2] = New_price
                                elif change == "count" :
                                    New_count = input("Enter the desired new count :")
                                    list2[3] = New_count
                                else :
                                    pass
                                li[Changing - 1] = list2
                                #print(li)
                                for i in range(len(li)-1):
                                    ch = ",".join(li[i])
                                    File.write(ch + "\n")
                                CH = ",".join(li[-1])
                                File.write(CH)
                                list_change.clear()
                                li.clear()
                                list2.clear()
                    else :
                        print("Not found !!")
        except Exception as e :
             print(e)
             list_change.clear()
             li.clear()
try :
    Store = Store()
    while True : 
            choos = input("Choose what you want to do (read_from_database,add,search,show_all,remove,update) : ")
            if choos == "read_from_database":
                print(Store.read_from_database())
            elif choos == "add":
                ID = input("enter id : ")
                NAME = input("enter name : ")
                PRICE = input("enter price : ")
                COUNT = input("enter count : ")
                Store.add(ID,NAME,PRICE,COUNT)
            elif choos == "search":
                Store.search()
            elif choos == "show_all":
                Store.show_all()
            elif choos == "remove":
                Store.remove()
            elif choos == "update":
                Store.update()
            else :
                print("Enter your choice correctly !!")
except Exception as e :
    print(e)