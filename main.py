import pygame
from pygame.locals import *
from sys import exit
from characters import *
from random import randint
import time
pygame.init()

FPS = 28 #Frames
fpsClock = pygame.time.Clock()


# Tamanho da Janela
DISPLAYSURF = pygame.display.set_mode([1000,508])
pygame.display.set_caption('Caça à Taça | Rafael Barbosa | Caio Alvares | Vitor Reginato')

#VARIAVEIS
WHITE = (255, 255, 255)

moveAux = 0


moveY=0

x = 10
y = 10

#Aguia Gaviao
a = Aguia()
a.animation()
a.deathAnimation()

inicio = Inicio()

bgr = Background(0,0)
bgr.animaBack()

cont = 0

cont2 =0.1

while True: 


    if inicio.init==False:
        bgr.draw(DISPLAYSURF)
        inicio.draw(DISPLAYSURF)
        for event in pygame.event.get():
            if event.type == KEYUP:
            
                if event.key == K_RETURN:
                    thief = Thief(DISPLAYSURF)
                    j = Friend(DISPLAYSURF)
                    
                    cards = []
                    for i in range (2):
                        yellow = Amarelo(DISPLAYSURF)
                        red = Vermelho(DISPLAYSURF)
                        cards.append(yellow)
                        cards.append(red)
                        
                    enemies = []
                    for i in range (3):
                        b = enemy(DISPLAYSURF)
                        enemies.append(b)
                    inicio.init=True
                    
    elif inicio.gameOver==True or a.hp==-10:

        bgr.draw(DISPLAYSURF)
        inicio.draw2(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == KEYUP:
            
                if event.key == K_RETURN:
                    cont2=0
                    bgr.round=1
                    thief = Thief(DISPLAYSURF)
                    b.hp=3
                    b.alive=True
                    j = Friend(DISPLAYSURF)
                    a.alive=True
                    a.hp=3
                    a.aux2=0
                    inicio.gameOver=False
                      
    else:


        xx,yy= pygame.mouse.get_pos()
    
        DISPLAYSURF.fill(WHITE)

        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_UP:
                    moveY=0
                    moveY-=5
                if event.key == K_DOWN:
                    moveY=0
                    moveY+=5

        if moveY < 0 and yy+26>0:
            y+=yy

        if moveY> 0 and yy+215<509:
            y+=yy
                    

        
        #Desenhos
        bgr.draw(DISPLAYSURF)
        a.draw(DISPLAYSURF,x,yy)
        j.draw()
        thief.draw()
        
        #Inimigos pigs
        for enemy in enemies:
            enemy.draw()

            #Colisão
            if enemy.rect.colliderect(a.rect) == True:
                a.hp-=enemy.dmg
                
                if a.hp<=0:
                    a.explode()
                enemy.hitOn()
                if a.hp==-10:
                    inicio.gameOver=True
                print(a.hp)


        if bgr.round > 1:
            #Inimigos cards
        
            for card in cards:
                card.draw()
                #Colisão
                if card.rect.colliderect(a.rect) == True:
                    a.hp-=card.dmg
                    if a.hp<=0:
                        a.explode()
                    card.hitOn()
                    if a.hp==-10:
                        inicio.gameOver=True
                    #print(a.hp)

        #Colisão Juiz
            
        if a.rect.colliderect(j.rect) == True:
            if a.hp<3:
                a.help()
            j.hitOn()
            #print(a.hp)
        
        if a.hp<=0:
            
            a.alive=False

        cont2+=0.1

        if cont2 >60.0 and cont2<100.0:
            bgr.round = 2
        if cont2>120.0:
            bgr.round=3

        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)











