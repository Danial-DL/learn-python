from media import Media
class Documentary(Media):
    def __init__(self,name,director,IMDB_score,url,duration,typeMovie):
        super().__init__(name,director,IMDB_score,url,duration,typeMovie)
        self.list_Documentary = []
    def DocumentaryMovie(self):
        if self.TYPE == "Documentary":
            self.list_Documentary.append(self.INF)
            print(f"list Documentary : {self.list_Documentary}")