from setting_movie import Movie
try :
    Movie = Movie()
    while True : 
            choos = input("Choose what you want to do (read_from_database,add,search,show_all,remove,update) : ")
            if choos == "read_from_database":
                print(Movie.read_from_database())
            elif choos == "add":
                #ID = input("enter id : ")
                NAME = input("enter name : ")
                DIRECTOR = input("enter director : ")
                IMDB = input("enter IMDB score : ")
                URL = input("enter url : ")
                DURATION = input("enrer duration : ")  
                num = int(input("Enter the number of actors : "))
                list_CASTS = []
                for i in range(num):
                    CASTS = input("enter casts : ")   
                    list_CASTS.append(CASTS)
                st = ",".join(list_CASTS)
                st2 = st.replace(",","_")
                while True:
                    TYPE = input("enter type movie : ")
                    if TYPE == "Serial" or TYPE == "Film" or TYPE == "Clip" or  TYPE == "Documentary" :
                        #list2[6] = TYPE
                        break
                    else :
                        print("not round type !!")
                Movie.add(NAME,DIRECTOR,IMDB,URL,DURATION,st2,TYPE)
            elif choos == "search":
                Movie.search()
            elif choos == "show_all":
                Movie.show_all()
            elif choos == "remove":
                Movie.remove()
            elif choos == "update":
                Movie.update()
            else :
                print("Enter your choice correctly !!")
except Exception as e :
    print(e)