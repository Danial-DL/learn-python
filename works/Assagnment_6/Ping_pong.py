import pygame
import random
pygame.init()
class Rocket:
    def __init__(self, x, y, color):
        
        self.h = 50
        self.w=10
        self.x = x
        self.y = y
        self.color = color
        self.speed = 100
        self.score = 0
        self.area =pygame.draw.rect(Game.screen, self.color, [self.x, self.y , self.w, self.h])
    def show(self):
        self.area =pygame.draw.rect(Game.screen, self.color, [self.x, self.y , self.w, self.h])
        
    def move(self, b) :
        if self.y < b.y :
            #self.y += self.speed
            self.y += 3
        elif self.y > b.y :
            #self.y -= self.speed
            self.y -= 3

class Color:
    red = (255, 0,0)
    blue = (0, 0,255)
    black = (0 ,0, 0)
    green = (0, 255,0)
    white = (255,255,255)
    yellow = (255,255,0)
class Ball:
    def __init__(self):
        self.r =10
        self.x= Game.width/2
        self.y = Game.height/2
        self.color = Color.green
        self.speed = 3
        self.select = random.choice(["plus","minus"])
        if self.select == "plus" :
            self.x_direction = 1
        elif self.select == "minus" :
            self.x_direction = -1
        self.y_direction = -1
        self.area = pygame.draw.circle(Game.screen, self.color, [self.x, self.y], self.r)
    def show(self):
        self.area = pygame.draw.circle(Game.screen, self.color, [self.x, self.y], self.r)
        
    def move(self):
        self.x += self.speed*self.x_direction
        self.y += self.speed*self.y_direction
        
        if self.y > Game.height or self.y < 0:
            self.y_direction *= -1
            
    def new(self):
        self.select = random.choice(["plus","minus"])
        if self.select == "plus" :
            self.x_direction = 1
        elif self.select == "minus" :
            self.x_direction = -1
        self.x = 0
        self.y = 0
        self.x= Game.width/2
        self.y = Game.height/2
class Score:
    def __init__ (self,scor_me,scor_computer,screen):
        me = Rocket(20, Game.height/2 , Color.red)
        computer = Rocket(Game.width-30, Game.height/2 , Color.blue)
        self.SCOR_me = me.score
        self.SCOR_computer = computer.score
        #
        game = Game()
        #ball = Ball()
        #if ball.x<0:
        #         game.play.computer.score += 1
        # #if ball.x>Game.width:
        #         game.play.me.score += 1        
        self.sc = screen
        
        #self.width = 700
        #self.height = 400
        #self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None,50)
        self.T_S_me = self.font.render(f"scor me : {scor_me}",True,(0,255,255))
        self.T_S_computer = self.font.render(f"scor computer : {scor_computer}",True,(100,100,100))
    def show(self):
        
        self.sc.blit(self.T_S_me,(10,20)) 
        self.sc.blit(self.T_S_computer,(360,20)) 
class Game:
    width = 700
    height = 400
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    fps = 50
    
    @staticmethod
    def play():
        me = Rocket(20, Game.height/2 , Color.red)
        computer = Rocket(Game.width-30, Game.height/2 , Color.blue)
        ball = Ball()
        game = Game()
        pygame.display.set_caption("Ping pong")
        #score.show()
        while True:
            pygame.mouse.set_visible(False)
            #score.show()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    me.y = pygame.mouse.get_pos()[1] 
                    if me.y > Game.height - me.h:
                        me.y = Game.height - me.h      
            font = pygame.font.Font(None,100)
            if ball.x<0:
                computer.score += 1

                ball.new()
                pygame.display.update()
            if ball.x>Game.width:
                me.score += 1

                #Score.show()
                ball.new()      
                pygame.display.update()
            score = Score(me.score,computer.score,game.screen)
            if me.area.colliderect(ball.area) :
                #
                ball.x_direction*=-1  
                ball.x += 1
                ball.move()
            elif computer.area.colliderect(ball.area) :
                #
                ball.x_direction*=-1  
                ball.x -= 1
                ball.move()
                    
            Game.screen.fill(Color.black)
            pygame.draw.rect(Game.screen, Color.yellow, [0 ,0, Game.width,Game.height],10)
            pygame.draw.aaline(Game.screen, Color.white,[Game.width/2 , 0], [Game.width/2, Game.height])
            #Score.show(0)
            me.show()
            computer.show()
            ball.show()
            ball.move()
            computer.move(ball)
            score.show()
            pygame.display.update()
            Game.clock.tick(Game.fps)
            pygame.display.flip()
            
            
if __name__=="__main__":
    Game.play()