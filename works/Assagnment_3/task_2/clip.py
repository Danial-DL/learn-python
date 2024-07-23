from media import Media
class Clip(Media):
    def __init__(self,name,director,IMDB_score,url,duration,typeMovie):
        super().__init__(name,director,IMDB_score,url,duration,typeMovie)
        self.list_Clip = []
    def clipMovie(self):
        if self.TYPE == "Clip":
            self.list_Clip.append(self.INF)
            print(f"list Clip : {self.list_Clip}")