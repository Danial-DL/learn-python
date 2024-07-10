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
        self.list_change = []
        self.li = []
        self.list2 = []
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
            self.list_search2 = []
            f = open("database_work_5.csv","r")
            big_text = f.read()
            self.product_list = big_text.split("\n")
            #print(self.product_list)
            for i in range(len(self.product_list)):
                info = self.product_list[i].split(",")
                #print(info)
                self.list_search2.append(info)
            #print(list_search2)
            input_search = input("What line are you looking for? Just enter one of the information inside and we will find it :")
            for i in self.list_search2:
                for x in i:
                    if x == input_search :
                        print(f"We have successfully found that relevant section {i}")
                    else :
                        pass
        except Exception as e :
            print(e)
            self.list_search2.clear()
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
            self.list_change = []
            self.li = []
            self.list2 = []
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
                                    self.list_change = i.split(",")
                                    self.li.append(self.list_change)
                                #print(li)
                                self.list2 = li[Changing - 1]
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
                                self.li[Changing - 1] = self.list2
                                #print(li)
                                for i in range(len(self.li)-1):
                                    ch = ",".join(self.li[i])
                                    File.write(ch + "\n")
                                CH = ",".join(self.li[-1])
                                File.write(CH)
                                self.list_change.clear()
                                self.li.clear()
                                self.list2.clear()
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