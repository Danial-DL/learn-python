class Store:
    def __init__(self):
        self.product = []
        self.list_input = []
        self.product_search = []
        #self.Previous_list = []
        self.list_change = []
        self.li = []
        self.list2 = []
    def read_from_database(self):
        try :
            f = open("dataset_work_5.csv","r")
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
    def add(self,id=None,name=None,price=None,count=None):
        try :
            self.product.clear()
            ID = id
            NAME = name
            PRICE = price
            COUNT = count
            self.product.append(ID)
            self.product.append(NAME)
            self.product.append(PRICE)
            self.product.append(COUNT)
            with open("dataset_work_5.csv","a") as file:
                for i in self.product:
                    a = ",".join(self.product)
                file.write("\n" + a )
                self.product.clear()
            #return self.product_list
        except Exception as e :
            self.product.clear()
            print(e)
    def search(self):
        try :
            self.product.clear()
            f = open("dataset_work_5.csv","r")
            big_text = f.read()
            self.product_list = big_text.split("\n")
            #print(self.product_list)
            for i in range(len(self.product_list)):
                info = self.product_list[i].split(",")
                #print(info)
                self.product.append(info)
            #print(list_search2)
            input_search = input("What line are you looking for? Just enter one of the information inside and we will find it :")
            for i in self.product:
                for x in i:
                    if x == input_search :
                        print(f"We have successfully found that relevant section {i}")
                    else :
                        pass
        except Exception as e :
            self.product.clear()
            print(e)
    def show_all(self):
        try :
            FILE = open("dataset_work_5.csv","r")
            print(FILE.read())
        except Exception as e :
            print(e)
    def remove(self):
        try :
            with open("dataset_work_5.csv","r") as File :
                line = File.readlines()
                num = len(line)
                trash_bin = int(input(f"This database has {num} rows, select the row you want to delete : "))
                if trash_bin > num or 0 >= trash_bin :
                    print("Not found")    
                else :
                    with open("dataset_work_5.csv","r") as File :
                        previous_state = File.read()
                        self.product_list = previous_state.split("\n")
                        #print(self.product_list)
                        del self.product_list[trash_bin - 1]
                        with open("dataset_work_5.csv","w") as File :
                            for i in range(len(self.product_list)-1):
                                File.write(self.product_list[i] + "\n") 
                            File.write(self.product_list[-1])
                            #print(self.product_list)
                            self.product_list.clear()
        except Exception as e:
            print(e)
            self.product_list.clear()
    def update(self):
        try :
            self.list_change.clear()
            self.li.clear()
            self.list2.clear()
            with open("dataset_work_5.csv","r") as File :
                line = File.readlines()
                num = len(line)
                Changing = int(input(f"This database has {num} rows, Select a row to change : "))
                if Changing > num or 0 >= Changing :
                    print("Not found") 
                else :
                    change = input("What do you want to change in the row (id,name,price,count) :")
                    if change == "id" or change == "name" or change == "price" or change == "count" :
                        with open("dataset_work_5.csv","r") as File :
                            previous_state = File.read()
                            self.product_list = previous_state.split("\n")
                            with open("dataset_work_5.csv","w") as File :
                                for i in self.product_list:
                                    self.list_change = i.split(",")
                                    self.li.append(self.list_change)
                                #print(li)
                                self.list2 = self.li[Changing - 1]
                                #print(list2)
                                if change == "id" :
                                    New_id = input("Enter the desired new ID :")
                                    self.list2[0] = New_id
                                elif change == "name" :
                                    New_name = input("Enter the desired new name :")
                                    self.list2[1] = New_name
                                elif change == "price" :
                                    New_price = input("Enter the desired new price :")
                                    self.list2[2] = New_price
                                elif change == "count" :
                                    New_count = input("Enter the desired new count :")
                                    self.list2[3] = New_count
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
             self.list_change.clear()
             self.li.clear()
             self.list2.clear()
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