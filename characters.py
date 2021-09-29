#import pygame
import random
import pygame
import os, sys
import random
import time

pygame.display.set_mode((1000,500))


############################################################################################################

class Background(object):

    def __init__(self,posX,posY):

        self.hino = pygame.mixer.Sound('sounds/hino.wav')
        self.hino.set_volume(0.3)
        pygame.mixer.Channel(3).play(self.hino, loops=-1)
        self.posX=posX
        self.posY=posY
        self.back=[]
        self.aux=0
        self.round=1
        

    def animaBack(self):
        for i in range(0,71,1):
            fundo = pygame.image.load('fundo/fundo'+str(i)+'.jpg')
            self.back.append(fundo)

    def draw(self,surface):
        self.fase = pygame.image.load('fundo/round'+str(self.round)+'.png').convert_alpha()
        if self.aux<len(self.back)-1:
            self.aux+=1
        else:
            self.aux=0

        surface.blit(self.back[self.aux],(self.posX,self.posY))
        surface.blit(self.fase,(0,0))
            
        

    def anima(self):

        if self.aux<len(self.back)-1:
            self.aux+=1
        else:
            self.aux=0
        return self.back[self.aux]

    def position(self):
        return self.posX,self.posY

#############################################################################################################################

class Inicio(object):

    def __init__(self):
        self.init = False
        self.gameOver = False
        self.posX=0
        self.posY=0
        self.inicio = pygame.image.load('telaInicial/source.png')
        self.restart = pygame.image.load('telaInicial/source2.png')
        self.win = pygame.image.load('telaInicial/source3.png')

    def draw(self,surface):
        surface.blit(self.inicio,(self.posX,self.posY))

    def draw2(self,surface):
        surface.blit(self.restart,(self.posX,self.posY))

    def draw3(self,surface):
        surface.blit(self.win,(self.posX,self.posY))
    
###########################################################################################################

class Aguia(object):
    
        
    def __init__(self):
        self.exp = pygame.mixer.Sound('sounds/explosion.wav')
        self.exp.set_volume(1.7)
        self.posX=10
        self.posY=random.randint(0,10)
        self.rect = pygame.Rect(self.posX,self.posY, 180, 114)
        self.alive=True
        self.hp=3
        self.dmgArt=True
        self.aguia=[]
        self.death=[]
        self.aux=0
        self.aux2=0
        self.move = 5
        


    def animation(self):
        for i in range(4,56,1):
            frame = pygame.image.load('aguia/aguia'+str(i)+'.png').convert_alpha()
            self.aguia.append(frame)

    def deathAnimation(self):
        for i in range(0,78,1):
            explode = pygame.image.load('effects/explode'+str(i)+'.png').convert_alpha()
            self.death.append(explode)
            #self.rect = frame.get_rect()

    def check(self):
        if(self.hp<=0):
            self.alive==False
            
    
    def draw(self,surface,x,y):
        self.x=x
        self.y=y
        if self.hp<0:
            self.hp=0
            self.life = pygame.image.load('effects/life'+str(self.hp)+'.png').convert_alpha()
        self.life = pygame.image.load('effects/life'+str(self.hp)+'.png').convert_alpha()
            
        #pygame.draw.rect(surface,(255,255,255),self.rect,2)
        if self.alive ==  True:
        
            if self.aux<len(self.aguia)-1:
                self.aux+=1
            else:
                self.aux=0

            self.rect = pygame.Rect(self.x,self.y, 180,150)
            
            surface.blit(self.life,(-20,0))
            surface.blit(self.aguia[self.aux],(self.x,self.y))

        else:
            #pygame.mixer.Channel(1).play(self.exp)
            if self.aux2<len(self.death)-1:
                self.aux2+=1

            if self.aux2 == 77:
                self.alive=False
                self.hp=-10


            
            surface.blit(self.life,(-20,0))
            surface.blit(self.death[self.aux2],(self.x,self.y))
            
            
            
        
    def up(self):
        self.move=0
        self.move=5
        if self.move>0 and self.posY+26>0:
            self.posY-=self.move
        #print(self.posY)

    def down(self):
        self.move=0
        self.move=5
        if self.move>0 and self.posY+215<509:
                self.posY+=self.move



    def explode(self):
        
        pygame.mixer.Channel(1).play(self.exp)
            #self.alive=False
    def help(self):
        self.hp+=1
            
        


###########################################################################################################

class enemy(object):
        
    def __init__(self,surface):
        self.hit = pygame.mixer.Sound('sounds/hit.wav')
        self.hit.set_volume(1.7)
        self.pig=pygame.image.load('enimies/pigfast.png').convert_alpha()
        self.px = random.randint(1000,1500)
        self.py = random.randint(-90,508)
        self.surface= surface
        self.rect = pygame.Rect(self.px,self.py, 62,62)
        self.surface =  surface
        self.dmg=1


    def draw(self):
        
        self.px-=5
        if self.px+163 <= 0:
            self.px=random.randint(1000,2000)
            self.py = random.randint(-90,508)

        #pygame.draw.rect(self.surface,(255,255,255),self.rect,2)
        self.surface.blit(self.pig,(self.px,self.py))
        self.rect = pygame.Rect(self.px,self.py, 62, 62)
      
    def hitOn(self):
        pygame.mixer.Channel(0).play(self.hit)
        self.px=random.randint(1000,2000)
        



#############################################################################################################


class Amarelo(object):
        
    def __init__(self,surface):
        self.hit = pygame.mixer.Sound('sounds/hit.wav')
        self.hit.set_volume(1.7)
        self.amarelo=pygame.image.load('enimies/amarelo.png').convert_alpha()
        self.px = random.randint(1500,2000)
        self.py = random.randint(-90,508)
        self.surface= surface
        self.rect = pygame.Rect(self.px,self.py, 30,41)
        self.surface =  surface
        self.dmg = 2


    def draw(self):
        
        self.px-=5
        if self.px+163 <= 0:
            self.px=random.randint(1000,2000)
            self.py = random.randint(-90,508)

        #pygame.draw.rect(self.surface,(255,255,255),self.rect,2)
        self.surface.blit(self.amarelo,(self.px,self.py))
        self.rect = pygame.Rect(self.px,self.py, 30, 41)
                
                
      
    def hitOn(self):
        pygame.mixer.Channel(0).play(self.hit)
        self.px=random.randint(1000,2000)


#####################################################################################################

class Vermelho(object):
        
    def __init__(self,surface):
        self.hit = pygame.mixer.Sound('sounds/hit.wav')
        self.hit.set_volume(1.7)
        self.vermelho=pygame.image.load('enimies/vermelho.png').convert_alpha()
        self.px = random.randint(1500,2000)
        self.py = random.randint(-90,508)
        self.surface= surface
        self.rect = pygame.Rect(self.px,self.py, 30,41)
        self.surface =  surface
        self.dmg = 3


    def draw(self):
        
        self.px-=5
        if self.px+163 <= 0:
            self.px=random.randint(1000,2000)
            self.py = random.randint(-90,508)

        #pygame.draw.rect(self.surface,(255,255,255),self.rect,2)
        self.surface.blit(self.vermelho,(self.px,self.py))
        self.rect = pygame.Rect(self.px,self.py, 30, 41)
                
                
      
    def hitOn(self):
        pygame.mixer.Channel(0).play(self.hit)
        self.px=random.randint(1000,2000)

 ##############################################################################################################

class Thief(object):
        
    def __init__(self,surface):

        self.pig=pygame.image.load('enimies/pigthief.png').convert_alpha()
        self.px = 100
        self.py = 200
        self.surface= surface
        self.rect = pygame.Rect(self.px,self.py, 62,62)
        self.surface =  surface


    def draw(self):
        
        self.px+=3
    
        if self.px<1100:
            #pygame.draw.rect(self.surface,(255,255,255),self.rect,2)
            self.surface.blit(self.pig,(self.px,self.py))
            self.rect = pygame.Rect(self.px,self.py, 62, 62)
        

##############################################################################################################

            
class Friend(object):
        
    def __init__(self,surface):
        self.hit = pygame.mixer.Sound('sounds/juiz.wav')
        self.hit.set_volume(1.7)
        self.juiz=pygame.image.load('friend/juiz.png').convert_alpha()
        self.px = random.randint(3000,5000)
        self.py = random.randint(300,508)
        self.rect = pygame.Rect(self.px,self.py, 63,100)
        self.surface =  surface
        self.bonus=1


    def draw(self):
        
        self.px-=7
        if self.px+163 <= 0:
            self.px=random.randint(3000,5000)
            self.py = random.randint(300,508)

        self.surface.blit(self.juiz,(self.px,self.py))
        self.rect = pygame.Rect(self.px,self.py, 63, 100)
        #pygame.draw.rect(self.surface,(255,255,255),self.rect,2) 
              
    
    def hitOn(self):
        pygame.mixer.Channel(4).play(self.hit)
        self.px=random.randint(3000,5000)


###########################################################################################################

        
        
    



        
        

        
