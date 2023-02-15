#Hello world



#x = int(input("x: "))
#y = int(input("y: "))
#print(x + y)

#entry = input("password : ")
#password = 'admin'
#if entry == password :
#    print(f"Welcome")
#else :
#    print(f"Wrong pasword")

#class Player :
#    def __init__(self) -> None:
#        self.pos = (2,2)
#    def attack(self):
#        print("attack")

import math
import pygame
import random

from pygame.constants import K_RIGHT, MOUSEBUTTONDOWN, K_j
from Player import Perso

module_charge = pygame.init()
print(module_charge)

#Init Game
ecran = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Survive Space 4000")

width = ecran.get_width() 
height = ecran.get_height() 

#Chrono
clock = pygame.time.Clock()
counter, text = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

#menu
text2 =font.render('Press Space to Play' , True , (0,0,0)) 
textlvl =font.render('LVL 2 -> Press Space' , True , (0,0,0))
textlv2 =font.render('LVL 3 -> Press Space' , True , (0,0,0))
textlv3 =font.render('Congrat, You finish the game !' , True , (0,0,0))

#music
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

#var
loop = False
game = True
reset = False
lvlup = 2
i = 0

#Player
p = Perso()
p.x = 500
p.y = 400

#Enemy
m = Perso() #yellow
m1 = Perso()#yellow
m2 = Perso()#yellow
m3 = Perso()#yellow
mb = Perso()#red
mb1 = Perso()#red
mc = Perso()#blue

#If they appear
m1v = False
m2v = False
m3v = False
mcv = False
mbwhere = random.randint(1,4)#whitch side ? (top, left, right, bot)

#the game it's self
while game :
    i += 1
    if lvlup < 0:
        lvlup = 0

    #reset if die or pause
    if reset:
        counter, text = 60, '60'.rjust(3)
        p.x = 500
        p.y = 400
        m.x = 0
        m.y = 250
        m1.y = -2000
        m2.y = 3000
        m3.x = 2400
        mb.x = 2000
        mb.y = 1100
        mb1.x = 2000
        mb1.y = 1100
        mc.x = 3000
        mc.y = 3000
        m1v = False
        m2v = False
        m3v = False
        mcv = False
        reset = False
        i = 0

    if loop: 
        #screen decoration
        ecran.fill((30,30,30))
        ecran.blit(font.render(text, True, (250, 250, 250)), (32, 48))

        #Chrono
        if pygame.event.get(pygame.USEREVENT) :
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Bravo !'
        if text == 'Bravo !' :
            loop = False
            lvlup += 1

        #Limitation deplacement
        if p.x < 0 :
            p.x = 0
        if p.x > 1000 :
            p.x = 1000
        if p.y < 0 :
            p.y = 0
        if p.y > 800 :
            p.y = 800

        #venu des enemy
        if counter == 50:
            m1.x = 0
            m1v = True
        if counter == 55:
            m2.x = 1000
            m2v = True
        if counter == 45:
            m3.x = 800
            m3v = True

        #speed of enemy
        if 15 < counter < 35 :
            m.x = m.x+8
            m1.y = m1.y + 8
            m2.y = m2.y - 8
            m3.x = m3.x - 8
        elif 0 < counter < 15 :
            m.x = m.x+10
            m1.y = m1.y + 10
            m2.y = m2.y - 10
            m3.x = m3.x - 10
        else :
            if lvlup > 0 :
                m.x = m.x+8
                m1.y = m1.y + 8
                m2.y = m2.y - 8
                m3.x = m3.x - 8
            else:
                m.x = m.x+6
                m1.y = m1.y + 6
                m2.y = m2.y - 6
                m3.x = m3.x - 6
            
        # + lvl 2 add red ennemies
        if lvlup > 0:
        
            if counter == 60 or 0:
                mb.x = 2000
                mb.y = 1100
                mb1.x = 2000
                mb1.y = 1100
            elif counter%5 == 1:
                mbwhere = random.randint(1,4)
            elif counter%5 == 0:
                if mbwhere == 1:
                    mb.x = 0
                    mb.y = random.randint(100,900)
                    mb1.x = 0
                    mb1.y = random.randint(100,900)
                if mbwhere == 2:
                    mb.x = 800
                    mb.y = random.randint(100,900)
                    mb1.x = 800
                    mb1.y = random.randint(100,900)
                if mbwhere == 3:
                    mb.x = random.randint(100,700)
                    mb.y = 0
                    mb1.x = random.randint(100,700)
                    mb1.y = 0
                if mbwhere == 4:
                    mb.x = random.randint(100,700)
                    mb.y = 1000
                    mb1.x = random.randint(100,700)
                    mb1.y = 1000
            
            elif counter%5 == 4:
                mb.x = mb.x
                mb.y = mb.y
                mb1.x = mb1.x
                mb1.y = mb1.y
                
            else:
                if mbwhere == 1:
                    mb.x += 30
                    mb1.x += 30
                if mbwhere == 2:
                    mb.x -= 30
                    mb1.x -= 30
                if mbwhere == 3:
                    mb.y += 30
                    mb1.y += 30
                if mbwhere == 4:
                    mb.y -= 30
                    mb1.y -= 30
        # + lvl 3 add blue ennemie
        if lvlup > 1:
            if counter == 56:
                mcv = False
                mc.x = 0
                mc.y = 0
            if mc.x < 400:
                mc.x += 8
                mc.y += 10
            if mc.x == 400:
                mcv = True
            if counter%7 >= 0 and mcv:
                mc.x = (pygame.time.get_ticks()/1000)%20 * math.sin((pygame.time.get_ticks()/1000)%20)*30 + width/2 
                mc.y = (pygame.time.get_ticks()/1000)%20 *  math.cos((pygame.time.get_ticks()/1000)%20)*30 + height/2

        #colisions
        distm = pow((p.x-(m.y))**2 + ((p.y)-m.x)**2, 0.5)
        if distm < 40 :
            loop = False
            lvlup -= 1
        distm1 = pow((p.x-(m1.y))**2 + ((p.y)-m1.x)**2, 0.5)
        if distm1 < 40 :
            loop = False
            lvlup -= 1
        distm2 = pow((p.x-(m2.y))**2 + ((p.y)-m2.x)**2, 0.5)
        if distm2 < 40 :
            loop = False
            lvlup -= 1
        distm3 = pow((p.x-(m3.y))**2 + ((p.y)-m3.x)**2, 0.5)
        if distm3 < 40 :
            loop = False
            lvlup -= 1
        distmb = pow((p.x-(mb.y))**2 + ((p.y)-mb.x)**2, 0.5)
        if distmb < 40 :
            loop = False
            lvlup -= 1
        distmb1 = pow((p.x-(mb1.y))**2 + ((p.y)-mb1.x)**2, 0.5)
        if distmb1 < 40 :
            loop = False
            lvlup -= 1
        distmc = pow((p.x-(mc.y))**2 + ((p.y)-mc.x)**2, 0.5)
        if distmc < 40 :
            loop = False
            lvlup -= 1


        #random apparition
        if m.x > 800 :
            m.x = 0
            m.y = random.randint(2,1000)
        if m1.y == -5 or m1.y > 1000:
            if m1v :
                m1.x = random.randint(2,800)
            else :
                m1.x = -1000
            m1.y = 0
        if m2.y == 4000 or m2.y < 0:
            if m2v :
                m2.x = random.randint(2,800)
            else :
                m2.x = 3000
            m2.y = 1000
        if m3.x == 1600 or m3.x < 0:
            if m3v :
                m3.x = 800
            else :
                m3.x = 2400
            m3.y =  random.randint(2,1000)

        #Deplacement of the Player
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_d]:
                p.x +=10  
            if pygame.key.get_pressed()[pygame.K_s]:
                p.y +=10  
            if pygame.key.get_pressed()[pygame.K_z]:
                p.y -=10  
            if pygame.key.get_pressed()[pygame.K_q]:
                p.x -=10  
            
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    loop = False
                if event.type == pygame.QUIT:
                    loop = False

        #Update & Draw
        p.Update()
        p.Draw(ecran)
        m.DrawEnemy(ecran)
        m1.DrawEnemy(ecran)
        m2.DrawEnemy(ecran)
        m3.DrawEnemy(ecran)
        mb.DrawBigEnemy(ecran)
        mb1.DrawBigEnemy(ecran)
        mc.DrawBossEnemy(ecran)
        pygame.display.flip()
        clock.tick(60)
    else:
        # Menu
        ecran.fill((200,200,200))
        if lvlup == 1:
            ecran.blit(textlvl , (width/2-width/6,height/2))
        elif lvlup == 2:
            ecran.blit(textlv2 , (width/2-width/6,height/2))
        else:
            ecran.blit(text2 , (width/2-width/6,height/2))
        pygame.display.flip()
        mouse = pygame.mouse.get_pos() 
        
        for event in pygame.event.get():            
            if event.type == pygame.KEYDOWN:
                
                if event.key== pygame.K_SPACE:
                    loop = True
                    reset = True
                if event.key== pygame.K_j:
                    game = False
                if event.type == pygame.QUIT:
                    game = False
        pygame.display.update() 
        

#quit the game
pygame.quit()