from documentary import Documentary
from clip import Clip
from film import Film
from serial import Serial
while True :
    #list_actors = [] 
    Enter_Name = input("Enter video Name : ")
    Enter_director = input("Enter video director : ")
    Enter_IMDB_score = input("Enter video IMDB_score : ")
    Enter_url = input("Enter video url (Link YouTube) : ")
    Enter_duration = input("Enter video duration : ")
    while True :
        Enter_type = input("Enter video type (Serial,Film,Clip,Documentary) : ")
        if Enter_type == "Serial" :
            Enter_part = input("Enter video part : ") # name,director,IMDB_score,url,duration,typeMovie,part
            Serial = Serial(Enter_Name,Enter_director,Enter_IMDB_score,Enter_url,Enter_duration,Enter_type,Enter_part)
            while True :
                select = input("Enter your choice : (showInfo , download , cut , List of series , list of actors , exit) : ")
                if select == "showInfo" :
                    Serial.showInfo()
                elif select == "download" :
                    Serial.download()
                elif select == "cut" :
                    first = int(input("Enter Number First minutes : ")) * 60
                    last = int(input("Enter Number last minutes : ")) * 60
                    Serial.cut(first,last)
                elif select == "List of series" :
                    Serial.serialMovie()
                elif select == "list of actors" :
                    Serial.casts()
                elif select == "exit" :
                    Serial.save()
                    #list_actors.clear()
                    break
                else :
                    print("Your selection was not found !!")
        elif Enter_type == "Film"  :
            Film =  Film(Enter_Name,Enter_director,Enter_IMDB_score,Enter_url,Enter_duration,Enter_type)
            while True :
                select = input("Enter your choice : (showInfo , download , cut , List of Film , list of actors , exit) : ")
                if select == "showInfo" :
                    Film.showInfo()
                elif select == "download" :
                    Film.download()
                elif select == "cut" :
                    first = int(input("Enter Number First minutes : ")) * 60
                    last = int(input("Enter Number last minutes : ")) * 60
                    Film.cut(first,last)
                elif select == "List of Film" :
                    Film.filmMovie()
                elif select == "list of actors" :
                    Film.casts()
                elif select == "exit" :
                    Film.save()
                    #list_actors.clear()
                    break
                else :
                    print("Your selection was not found !!")
        elif Enter_type == "Clip" :
            Clip =  Clip(Enter_Name,Enter_director,Enter_IMDB_score,Enter_url,Enter_duration,Enter_type)
            while True :
                select = input("Enter your choice : (showInfo , download , cut , List of Clip  , list of actors , exit) : ")
                if select == "showInfo" :
                    Clip.showInfo()
                elif select == "download" :
                    Clip.download()
                elif select == "cut" :
                    first = int(input("Enter Number First minutes : ")) * 60
                    last = int(input("Enter Number last minutes : ")) * 60
                    Clip.cut(first,last)
                elif select == "List of Clip" :
                    Clip.clipMovie()
                elif select == "list of actors" :
                    Clip.casts()
                elif select == "exit" :
                    Clip.save()
                    #list_actors.clear()
                    break
                else :
                    print("Your selection was not found !!")
        elif Enter_type == "Documentary" :
            Documentary =  Documentary(Enter_Name,Enter_director,Enter_IMDB_score,Enter_url,Enter_duration,Enter_type)
            while True :
                select = input("Enter your choice : (showInfo , download , cut , List of Documentary , list of actors , exit) : ")
                if select == "showInfo" :
                    Documentary.showInfo()
                elif select == "download" :
                    Documentary.download()
                elif select == "cut" :
                    first = int(input("Enter Number First minutes : ")) * 60
                    last = int(input("Enter Number last minutes : ")) * 60
                    Documentary.cut(first,last)
                elif select == "List of Documentary" :
                    Documentary.DocumentaryMovie()
                elif select == "list of actors" :
                    Documentary.casts()
                elif select == "exit" :
                    Documentary.save()
                    #list_actors.clear()
                    break
                else :
                    print("Your selection was not found !!")
        break
    else :
        print("not found type !!")