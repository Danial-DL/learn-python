import pytube
from moviepy.editor import *
import os
class Actor:
    def __init__(self):
        #super().__init__(name=None,director=None,IMDB_score=None,url=None,duration=None,casts=None,typeMovie=None)
        #self.casts = casts
        self.list_actors = []
    def casts(self):
        # num_casts = int(input("Enter the number of actors : "))
        # for i in range(num_casts) :
        #     name_casts = input("Enter the actor's name : ")
        Enter_Number_casts = int(input("Enter the number of actors : "))
        for i in range(Enter_Number_casts) :
            Enter_casts = input(f" Numer {i} Enter video cast : ")
            list_actors.append(Enter_casts)
            #self.list_casts.append(self)
        print(self.list_actors)
class Media(Actor):
    def __init__(self,name,director,IMDB_score,url,duration,casts,typeMovie):
        super().__init__()
        self.NAME = name
        self.DIRECTOR = director
        self.IMDB_SCORE = IMDB_score
        self.URL = url
        self.DURATION = duration
        #self.CASTS = []
        #self.CASTS.append(casts)
        self.TYPE = typeMovie
        #self.login = os.getlogin()
        #self.link = LINK
        #self.PATH = path
        self.pathFile = os.getcwd()
        self.INF = {"video Name" : self.NAME , "director" : self.DIRECTOR , "IMDB_score" : self.IMDB_SCORE , "url" : url , "duration" : self.DURATION ,  "casts" : str(self.list_actors) , "type" : self.TYPE}
        self.list_info = []
    def save(self):
        for i in self.INF.values():
            self.list_info.append(i)
        #print(self.list_info)
        with open("dataset_work_8.csv","a") as file:
                for i in self.list_info:
                    a = ",".join(self.list_info)
                file.write("\n" + a )
                self.list_info.clear()

    def showInfo(self):
        print(f"video Name : {self.NAME} , director  : {self.DIRECTOR} , IMDB_score : {self.IMDB_SCORE} , url : {self.URL} , duration : {self.DURATION} ,  casts : {self.list_casts} , type : {self.TYPE}")
    def download(self):
        pytube.YouTube(self.URL).stream.first().download(self.pathFile)
    def cut(self):
        clip = VideoFileClip(self.pathFile)
        sub = clip.subclip(a,b)
        num = 1
        while True:
            if os.path.exists(f"{self.pathFile}/movie{num}.mp4") :
                num += 1
                continue
            else :
                sub.write_videofile(f"{self.pathFile}/movie{num}.mp4")
                break
class Serial(Media):
    def __init__(self,name,director,IMDB_score,url,duration,typeMovie,part):
        super().__init__(name,director,IMDB_score,url,duration,typeMovie)
        self.PART = part
        self.list_serial = []
    def serialMovie(self):
        if self.TYPE == "Serial":
            self.list_serial.append(self.INF)
        print(f"list serial : {self.list_serial}")
class Film(Media):
    def __init__(self,name,director,IMDB_score,url,duration,typeMovie):
        super().__init__(name,director,IMDB_score,url,duration,typeMovie)
        self.list_Film = []
    def filmMovie(self):
        if self.TYPE == "Film":
            self.list_Film.append(self.INF)
            print(f"list Film : {self.list_Film}")
class Clip(Media):
    def __init__(self,name,director,IMDB_score,url,duration,typeMovie):
        super().__init__(name,director,IMDB_score,url,duration,typeMovie)
        self.list_Clip = []
    def clipMovie(self):
        if self.TYPE == "Clip":
            self.list_Clip.append(self.INF)
            print(f"list Clip : {self.list_Clip}")
class Documentary(Media):
    def __init__(self,name,director,IMDB_score,url,duration,typeMovie):
        super().__init__(name,director,IMDB_score,url,duration,typeMovie)
        self.list_Documentary = []
    def DocumentaryMovie(self):
        if self.TYPE == "Documentary":
            self.list_Documentary.append(self.INF)
            print(f"list Documentary : {self.list_Documentary}")
while True :
    list_actors = [] 
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
                select = input("Enter your choice : (showInfo , download , cut , save , List of series , list of actors , exit) : ")
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
                    list_actors.clear()
                    break
                else :
                    print("Your selection was not found !!")
        elif Enter_type == "Film"  :
            Film =  Film(Enter_Name,Enter_director,Enter_IMDB_score,Enter_url,Enter_duration,list_actors,Enter_type)
            while True :
                select = input("Enter your choice : (showInfo , download , cut , save , List of Film , list of actors , exit) : ")
                if select == "showInfo" :
                    Film.showInfo()
                elif select == "download" :
                    Film.download()
                elif select == "cut" :
                    first = int(input("Enter Number First minutes : ")) * 60
                    last = int(input("Enter Number last minutes : ")) * 60
                    Film.cut(first,last)
                elif select == "List of series" :
                    Film.filmMovie()
                elif select == "list of actors" :
                    Film.casts()
                elif select == "exit" :
                    Film.save()
                    list_actors.clear()
                    break
                else :
                    print("Your selection was not found !!")
        elif Enter_type == "Clip" :
            Clip =  Clip(Enter_Name,Enter_director,Enter_IMDB_score,Enter_url,Enter_duration,list_actors,Enter_type)
            while True :
                select = input("Enter your choice : (showInfo , download , cut , save , List of Film  , list of actors , exit) : ")
                if select == "showInfo" :
                    Clip.showInfo()
                elif select == "download" :
                    Clip.download()
                elif select == "cut" :
                    first = int(input("Enter Number First minutes : ")) * 60
                    last = int(input("Enter Number last minutes : ")) * 60
                    Clip.cut(first,last)
                elif select == "List of series" :
                    Clip.clipMovie()
                elif select == "list of actors" :
                    Clip.casts()
                elif select == "exit" :
                    Clip.save()
                    list_actors.clear()
                    break
                else :
                    print("Your selection was not found !!")
        elif Enter_type == "Documentary" :
            Documentary =  Documentary(Enter_Name,Enter_director,Enter_IMDB_score,Enter_url,Enter_duration,list_actors,Enter_type)
            while True :
                select = input("Enter your choice : (showInfo , download , cut , save , List of Film , list of actors , exit) : ")
                if select == "showInfo" :
                    Documentary.showInfo()
                elif select == "download" :
                    Documentary.download()
                elif select == "cut" :
                    first = int(input("Enter Number First minutes : ")) * 60
                    last = int(input("Enter Number last minutes : ")) * 60
                    Documentary.cut(first,last)
                elif select == "List of series" :
                    Documentary.DocumentaryMovie()
                elif select == "list of actors" :
                    Documentary.casts()
                elif select == "exit" :
                    Documentary.save()
                    list_actors.clear()
                    break
                else :
                    print("Your selection was not found !!")
        break
    else :
        print("not found type !!")