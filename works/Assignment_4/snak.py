import pygame
import random
import time
class Poison : 
    def __init__(self):
        self.r = 10
        self.width = 600
        self.height = 400
        self.display = pygame.display.set_mode((self.width, self.height))
        self.x = random.randint(0 , self.width)
        self.y = random.randint(0, self.height)
        self.color = (255,0,255)
    def show(self):
        pygame.draw.circle(self.display , self.color , [self.x , self.y], self.r) 
class Apple :
    def __init__(self):
        self.r = 10
        self.width = 600
        self.height = 400
        self.display = pygame.display.set_mode((self.width, self.height))
        self.x = random.randint(0 , self.width)
        self.y = random.randint(0, self.height)
        self.color = (255,0,0)
    def show(self):
        pygame.draw.circle(self.display, self.color, [self.x, self.y], self.r) 
class Snak:
    def __init__(self):
        self.w = 16
        self.h = 16
        self.width = 600
        self.height = 400
        self.display = pygame.display.set_mode((self.width, self.height))
        self.x = self.width /2
        self.y = self.height/2
        self.name = "python"
        self.color = (255, 255, 0)
        self.speed = 1
        self.score = 0
        self.x_change = 0
        self.y_change = 0
        self.body = []
        self.power = 50
    def eat(self):
        if (apple.x - apple.r <= self.x <= apple.x + apple.r) and (apple.y - apple.r <= self.y <= apple.y + apple.r):
            self.score +=1
            return True
        elif (poison.x - poison.r <= self.x <= poison.x +poison.r) and (poison.y - poison.r <= self.y <= poison.y + poison.r):
            self.score -= 1
            return False
    def show(self):
        pygame.draw.rect(self.display,self.color, [self.x , self.y , self.w , self.h])        
        for item in self.body:
             pygame.draw.rect(self.display,self.color, [item["x"], item["y"] , self.w , self.h])
    def move(self):
        self.body.append({"x":self.x,"y":self.y})
        if len(self.body) > self.score:
            self.body.remove(self.body[0])
            
        if self.x_change == -1:
            self.x-=self.speed
        elif self.x_change == 1:
            self.x +=self.speed
        elif self.y_change== -1:
            self.y-=self.speed
        elif self.y_change == 1:
            self.y+=self.speed
class Score:
    def __init__ (self):
        self.SCOR = snak.score    
    def show(self):
        font = pygame.font.Font(None,50)
        T_S = font.render(f"scor Game : {self.SCOR}",True,(0,0,255))
        display.blit(T_S,(10,20)) 
class GameOver :
    def __init__(self):
        self.scorGame = snak.score 
    def show(self):
        if snak.score < 0 or 0 >= snak.x or snak.x >= 590 or 0 >= snak.y or snak.y >= 390 :
            font_ower = pygame.font.Font(None,100)
            T_S_ower = font_ower.render("Game over !!",True,(255,0,0))
            display.blit(T_S_ower,(100,200))
            pygame.display.update()
            time.sleep(0.5)
            # Snak
            snak.w = 16
            snak.h = 16
            snak.width = 600
            snak.height = 400
            snak.display = pygame.display.set_mode((snak.width, snak.height))
            snak.x = snak.width /2
            snak.y = snak.height/2
            snak.name = "python"
            snak.color = (255, 255, 0)
            snak.speed = 1
            snak.score = 0
            snak.x_change = 0
            snak.y_change = 0
            snak.body = []
            snak.power = 50
            # poison
            poison.r = 10
            poison.width = 600
            poison.height = 400
            poison.display = pygame.display.set_mode((poison.width, poison.height))
            poison.x = random.randint(0 , poison.width)
            poison.y = random.randint(0, poison.height)
            poison.color = (255,0,255)
            # apple
            apple.r = 10
            apple.width = 600
            apple.height = 400
            apple.display = pygame.display.set_mode((apple.width, apple.height))
            apple.x = random.randint(0 , apple.width)
            apple.y = random.randint(0, apple.height)
            apple.color = (255,0,0) 
            # score
            score.SCOR = snak.score   
# ==============================================================================================
pygame.init()
# 
width = 600
height = 400
display = pygame.display.set_mode((width, height))
clock  = pygame.time.Clock()
snak = Snak()
apple = Apple()
poison = Poison()
score = Score()

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
                    exit()
        if event.type == pygame.KEYDOWN:
            # print(event)
            if event.key == pygame.K_UP:
                # print(event)
                snak.y_change= -1
                snak.x_change = 0
            elif event.key == pygame.K_DOWN:
                    snak.y_change = 1
                    snak.x_change = 0
            elif event.key == pygame.K_LEFT:
                snak.x_change = -1
                snak.y_change =0
            elif event.key == pygame.K_RIGHT:
                    snak.x_change = 1
                    snak.y_change = 0
    snak.move()
    result = snak.eat()
    game_over = GameOver()
    if result == True:
        apple = Apple()  
        score = Score()
        snak.power += 10
    elif result == False :  
        poison = Poison() 
        score = Score()       
        snak.power -= 10
    display.fill((0, 255,0))
    snak.show() 
    apple.show()
    poison.show()
    score.show()
    game_over.show()
    pygame.display.update()
    clock.tick(snak.power)                    