class Store:
    def __init__(self):
        self.movie = []
        self.list_input = []
        self.product_search = []
        #self.Previous_list = []
        self.list_change = []
        self.li = []
        self.list2 = []
    def read_from_database(self):
        try :
            f = open("dataset_work_8.csv","r")
            big_text = f.read()
            self.product_list = big_text.split("\n")
            #print(product_list)
            for i in range(len(self.product_list)):
                info = self.product_list[i].split(",")
                #print(info)
                self.movie.append({"video name" : info[0] , "director" : info[1] , "IMDB score" : info[2] , "url" : info[3] , "duration" : info[4] , "casts" : info[5] , "type" : info[6]})
            return self.movie
            #print(self.product)
        except Exception as e :
            print(e)
            self.movie= []
            return self.movie
            print(self.movie)
        #print(self.product)
    def add(self,name=None,director=None,score=None,url=None,duration=None,casts=None,typeMovie=None):
        try :
            self.movie.clear()
            #ID = id
            NAME = name
            DIRECTOR = director
            IMDB = score
            URL = url
            DURATION = duration
            CASTS = casts
            TYPE = typeMovie
            #self.movie.append(ID)
            self.movie.append(NAME)
            self.movie.append(DIRECTOR)
            self.movie.append(IMDB)
            self.movie.append(URL)
            self.movie.append(DURATION)
            self.movie.append(CASTS)
            self.movie.append(TYPE)
            with open("dataset_work_8.csv","a") as file:
                for i in self.movie:
                    a = ",".join(self.movie)
                file.write("\n" + a )
                self.movie.clear()
            #return self.product_list
        except Exception as e :
            self.movie.clear()
            print(e)
    def search(self):
        try :
            self.movie.clear()
            f = open("dataset_work_8.csv","r")
            big_text = f.read()
            self.product_list = big_text.split("\n")
            #print(self.product_list)
            for i in range(len(self.product_list)):
                info = self.product_list[i].split(",")
                #print(info)
                self.movie.append(info)
            #print(list_search2)
            input_search = input("What line are you looking for? Just enter one of the information inside and we will find it :")
            for i in self.movie:
                for x in i:
                    if x == input_search :
                        print(f"We have successfully found that relevant section {i}")
                    else :
                        pass
        except Exception as e :
            self.movie.clear()
            print(e)
    def show_all(self):
        try :
            FILE = open("dataset_work_8.csv","r")
            print(FILE.read())
        except Exception as e :
            print(e)
    def remove(self):
        try :
            with open("dataset_work_8.csv","r") as File :
                line = File.readlines()
                num = len(line)
                trash_bin = int(input(f"This database has {num} rows, select the row you want to delete : "))
                if trash_bin > num or 0 >= trash_bin :
                    print("Not found")    
                else :
                    with open("dataset_work_8.csv","r") as File :
                        previous_state = File.read()
                        self.product_list = previous_state.split("\n")
                        #print(self.product_list)
                        del self.product_list[trash_bin - 1]
                        with open("dataset_work_8.csv","w") as File :
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
            with open("dataset_work_8.csv","r") as File :
                line = File.readlines()
                num = len(line)
                Changing = int(input(f"This database has {num} rows, Select a row to change : "))
                if Changing > num or 0 >= Changing :
                    print("Not found") 
                else :
                    change = input("What do you want to change in the row (name,director,IMDB score,url,duration,casts,type) :")
                    if change == "name" or change == "director" or change == "IMDB score" or change == "url" or change == "duration" or change == "casts" or change == "type" :
                        with open("dataset_work_8.csv","r") as File :
                            previous_state = File.read()
                            self.product_list = previous_state.split("\n")
                            with open("dataset_work_8.csv","w") as File :
                                for i in self.product_list:
                                    self.list_change = i.split(",")
                                    self.li.append(self.list_change)
                                #print(li)
                                self.list2 = self.li[Changing - 1]
                                #print(list2)
                                if change == "name" :
                                    New_name = input("Enter the desired new name :")
                                    self.list2[0] = New_name
                                elif change == "director" :
                                    New_director = input("Enter the desired new director :")
                                    self.list2[1] = New_director
                                elif change == "IMDB score" :
                                    New_IMDBscore = input("Enter the desired new IMDB score :")
                                    self.list2[2] = IMDBscore
                                elif change == "url" :
                                    New_url = input("Enter the desired new url :")
                                    self.list2[3] = New_url
                                elif change == "duration" :
                                    New_duration = input("Enter the desired new duration :")
                                    self.list2[4] = New_duration
                                elif change == "casts" :
                                    New_casts = input("Enter the desired new casts :")
                                    self.list2[5] = New_casts
                                elif change == "type" :
                                    New_type = input("Enter the desired new type :")
                                    self.list2[6] = New_type
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
# ==================================================================================================================
# ==================================================================================================================
try :
    Store = Store()
    while True : 
            choos = input("Choose what you want to do (read_from_database,add,search,show_all,remove,update) : ")
            if choos == "read_from_database":
                print(Store.read_from_database())
            elif choos == "add":
                #ID = input("enter id : ")
                NAME = input("enter name : ")
                DIRECTOR = input("enter director : ")
                IMDB = input("enter IMDB score : ")
                URL = input("enter url : ")
                DURATION = input("enrer duration : ")  
                CASTS = input("enter casts : ")          
                Store.add(NAME,DIRECTOR,IMDB,URL,DURATION,CASTS)
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