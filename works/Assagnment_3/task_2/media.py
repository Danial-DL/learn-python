import pytube
from moviepy.editor import *
import os
from actor import Actor
class Media :
    def __init__(self,name,director,IMDB_score,url,duration,typeMovie):
        #super().__init__()
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
        self.A = Actor.casts()
        self.pathFile = os.getcwd()
        self.INF = {"video Name" : self.NAME , "director" : self.DIRECTOR , "IMDB_score" : self.IMDB_SCORE , "url" : url , "duration" : self.DURATION ,  "casts" : self.A , "type" : self.TYPE}
        self.list_info = list(self.INF.values())
    def save(self):
        # for i in self.INF.values():
        #     self.list_info.append(i)
        #print(self.list_info)
        #self.list_info = list(self.INF.values())
        print(self.list_info)
        with open("dataset_work_8.csv","a") as file:
            for i in self.list_info:
                a = ",".join(self.list_info)
            print(a)
            file.write("\n" + a )
            self.list_info.clear()
    def showInfo(self):
        print(f"video Name : {self.NAME} , director  : {self.DIRECTOR} , IMDB_score : {self.IMDB_SCORE} , url : {self.URL} , duration : {self.DURATION} ,  casts : {self.A} , type : {self.TYPE}")
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
    def casts(self):
        list_Ators = self.A.split("_")
        print(list_Ators)
        list_Ators.clear()
#
#
#
#
##