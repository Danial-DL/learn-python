class Actor:
    # def __init__():
    #     #super().__init__(name=None,director=None,IMDB_score=None,url=None,duration=None,casts=None,typeMovie=None)
    #     #self.casts = casts
    #     list_actors = []
    def casts():
        # num_casts = int(input("Enter the number of actors : "))
        # for i in range(num_casts) :
        #     name_casts = input("Enter the actor's name : ")
        list_actors = []
        Enter_Number_casts = int(input("Enter the number of actors : "))
        for i in range(Enter_Number_casts) :
            Enter_casts = input(f" Numer {i+1} Enter video cast : ")
            list_actors.append(Enter_casts)
        B = ",".join(list_actors)
        outpot = B.replace(",","_")
        #self.list_casts.append(self)
        return outpot
        #print(outpot)