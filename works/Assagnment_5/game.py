import pygame
import random
import os
import time
pathFile = os.getcwd()
PathPy = pathFile.replace("\\","/")
print(PathPy)
# print(pathFile)
#print("C:/Users/AliReza-PC/Desktop/python_project/works/Game/main.py")
pygame.init()
class Score:
    def __init__ (self):
        #self.SCOR = snak.score    
        self.SCOR = 0
    def show(self):
        font = pygame.font.Font(None,50)
        T_S = font.render(f"scor Game : {self.SCOR}",True,(0,0,255))
        game.display.blit(T_S,(10,20)) 
class Sound :
    def __init__(self):
        self.SOUND = pygame.mixer.Sound(f"{PathPy}/sound/gunshot.mp3")
    def show(self):
        self.SOUND.play()
        #time.sleep(self.SOUND.get_length())

class Character:
    def __init__(self,img):
        self.pathFile = os.getcwd()
        self.image = pygame.image.load(f"{PathPy}/images/{img}")
        self.x = 0
        self.y = random.randint(100,300)
        #self.x += 1
        self.new_width = 80
        self.new_height = 80
        self.scaled_image = pygame.transform.scale(self.image , (self.new_width, self.new_height))
    def show(self):
        game.display.blit(self.scaled_image, [self.x , self.y])
class Witch(Character):
    def __init__(self,img):
        super().__init__(img)
        #self.image = img
        #self.name = "Wich1.png"
class Bat(Character):
    def __init__(self,img):
        super().__init__(img)
        #self.image = img
class Angel(Character):
    def __init__(self,img):
        super().__init__(img)
        #self.image = img
class Gun:
    def __init__(self):
        #self.pathFile = os.getcwd()
        self.x = game.width/2
        self.y = game.height/2
        #self.image = pygame.image.load(f"{self.pathFile}/images/sniper.png")
        self.image = pygame.image.load(f"{PathPy}/images/sniper.png")
        self.new_width = 80
        self.new_height = 80
        self.scaled_image = pygame.transform.scale(self.image, (self.new_width, self.new_height))
        
        
    def show(self):
        game.display.blit(self.scaled_image, [self.x , self.y])

class Game:
    def __init__(self):
        self.width = 700
        self.height = 431
        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(f"{PathPy}/images/background.jpg")
        self.fps = 30
        
        
        
    def play (self):
        sound = Sound()
        score = Score()
        while True:
            pygame.mouse.set_visible(False)
            pygame.display.flip()
            select = ["witch","bat","Angel"]
            Chois = random.choice(select)
            if Chois == "witch":
                path_img = "Witch2.png"
                witch = Witch(path_img)
            elif Chois == "bat":
                path_img2 = "bat2.png"
                bat = Bat(path_img2)      
            elif Chois == "Angel":
                path_img3 = "angel.png"
                angel = Angel(path_img3)
            my_gun = Gun()
            while True:     
                #character = Character(x,y)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                        
                if event.type == pygame.MOUSEMOTION:
                        x , y = pygame.mouse.get_pos()
                        my_gun.x = x - 20
                        my_gun.y = y - 20
                        #sound.show()
                        
                self.display.blit(self.background, (0,0))
                if Chois == "witch": 
                    #witch.x += random.randint(1,10)
                    witch.x += 10
                    if witch.x == 700:
                        break
                    witch.show()
                    # if (witch.x >= my_gun.x < 2 or my_gun.x >= witch.x > -2) and (witch.y >= my_gun.y < 2 or my_gun.y >= witch.y > -2) and event.type==pygame.MOUSEBUTTONDOWN:
                    if (witch.x >= my_gun.x and my_gun.x < 10 or  witch.x >= my_gun.x and my_gun.x > -10) and (witch.y >= my_gun.y and my_gun.y < 10 or witch.y >= my_gun.y and my_gun.y > -10) and event.type==pygame.MOUSEBUTTONDOWN:
                        score.SCOR += 1 
                        # صدای شلیک
                        sound.show()
                        break
                if Chois == "bat":
                    #bat.x += random.randint(1,10)
                    bat.x += 10
                    if bat.x == 700:
                        break
                    # if (bat.x >= my_gun.x < 2 or my_gun.x >= bat.x > -2) and (bat.y >= my_gun.y < 2 or my_gun.y >= bat.y > -2) and event.type==pygame.MOUSEBUTTONDOWN:
                    if (bat.x >= my_gun.x and my_gun.x < 10 or  bat.x >= my_gun.x and my_gun.x > -10) and (bat.y >= my_gun.y and my_gun.y < 10 or bat.y >= my_gun.y and my_gun.y > -10) and event.type==pygame.MOUSEBUTTONDOWN:

                        score.SCOR += 1 
                        # صدای شلیک
                        sound.show()
                        break
                    bat.show()
                #print(type(witch.x))
                #print(type(bat.x))
                if Chois == "Angel":
                    angel.x += 10
                    if angel.x == 700:
                        break
                    # if (angel.x >= my_gun.x < 2 or my_gun.x >= angel.x > -2) and (angel.y >= my_gun.y < 2 or my_gun.y >= angel.y > -2) and event.type==pygame.MOUSEBUTTONDOWN:
                    if (angel.x >= my_gun.x and my_gun.x < 10 or  angel.x >= my_gun.x and my_gun.x > -10) and (angel.y >= my_gun.y and my_gun.y < 10 or angel.y >= my_gun.y and my_gun.y > -10) and event.type==pygame.MOUSEBUTTONDOWN:

                        score.SCOR -= 1 
                        # صدای شلیک
                        sound.show()
                        if score.SCOR < 0 :
                            score.SCOR = 0
                        break
                    angel.show()
                score.show()
                my_gun.show()
                pygame.display.update()
                self.clock.tick(self.fps)
                    
if __name__=="__main__":
    game = Game()
    game.play()    
    