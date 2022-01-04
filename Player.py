import pygame
class Perso:
    def __init__(self) -> None:
        self.x =2000
        self.y =2000
        self.vit =1
        self.dir ="none"


    def Draw(self, ecran) :
        pygame.draw.circle(ecran, (255,255,255), (self.x,self.y), 20)
    def DrawEnemy(self, ecran) :
        pygame.draw.circle(ecran, (255,255,0), (self.y,self.x), 20)
    def DrawBigEnemy(self, ecran) :
        pygame.draw.circle(ecran, (255,0,0), (self.y,self.x), 20)
    def DrawBossEnemy(self, ecran) :
        pygame.draw.circle(ecran, (135,206,250), (self.y,self.x), 20)

    def Update(self):
        if self.dir == 'up':
            self.y-=self.vit
        elif self.dir == "down":
            self.y+= self.vit
        elif self.dir == "left":
            self.x-= self.vit
        elif self.dir == "right":
            self.x+= self.vit
        