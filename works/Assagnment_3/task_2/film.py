from media import Media
class Film(Media):
    def __init__(self,name,director,IMDB_score,url,duration,typeMovie):
        super().__init__(name,director,IMDB_score,url,duration,typeMovie)
        self.list_Film = []
    def filmMovie(self):
        if self.TYPE == "Film":
            self.list_Film.append(self.INF)
            print(f"list Film : {self.list_Film}")