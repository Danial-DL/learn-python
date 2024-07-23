from media import Media
class Serial(Media):
    def __init__(self,name,director,IMDB_score,url,duration,typeMovie,part):
        super().__init__(name,director,IMDB_score,url,duration,typeMovie)
        self.PART = part
        self.list_serial = []
    def serialMovie(self):
        if self.TYPE == "Serial":
            self.list_serial.append(self.INF)
        print(f"list serial : {self.list_serial}")