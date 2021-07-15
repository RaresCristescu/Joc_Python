import pygame
import time
import random
import math


pygame.init()

lungime=800
inaltime=600

gameScreen=pygame.display.set_mode((lungime,inaltime));#vrea un tuplu inaunturu
pygame.display.set_caption("Hephaestus")


white=(255,255,255)
black=(0,0,0)
red=(250,0,0)
green=(0,185,0)

size_of_block = 25

clock = pygame.time.Clock()

font=pygame.font.SysFont(None,25)



def mesaj_ecran(msg,type):
    screen_text=font.render(msg,True,type)
    gameScreen.blit(screen_text,[lungime/2-5,inaltime/2-5])

def sarpe(snakeList,size_of_block):
    for xy in snakeList:
        pygame.draw.rect(gameScreen,green,[xy[0],xy[1],size_of_block,size_of_block])


def gameLoop():
    FPS = 15
    close=False
    gameOver = False
    lead_x = lungime / 2
    lead_y = inaltime / 2
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLenght= 1
    marX= round(random.randrange(0,lungime-size_of_block)/size_of_block)*size_of_block
    marY= round(random.randrange(0,inaltime-size_of_block)/size_of_block)*size_of_block

    while not close:
        while gameOver==True:
            gameScreen.fill(white)
            mesaj_ecran("Game Over press space to play again or Q to quit",black)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    close = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameOver=False
                        close=True
                    if event.key==pygame.K_SPACE:
                        gameLoop()




        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    lead_x_change=-size_of_block
                    lead_y_change = 0
                if event.key==pygame.K_RIGHT:
                    lead_x_change =size_of_block
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    lead_y_change = -size_of_block
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y_change =size_of_block
                    lead_x_change = 0
            # if event.type==pygame.KEYUP:
            #     if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
            #         lead_x_change=0
            #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #         lead_y_change =0
        if lead_x >=lungime or lead_x<0 or lead_y>=inaltime or lead_y<0:
            gameOver=True

        lead_x += lead_x_change
        lead_y+=lead_y_change
        gameScreen.fill(white)
        pygame.draw.rect(gameScreen,red,(marX,marY,size_of_block,size_of_block))
        pygame.display.update()


        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList)>snakeLenght:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment==snakeHead:
                gameOver=True

        sarpe(snakeList,size_of_block)
        pygame.display.update()
        if lead_x==marX and lead_y==marY:
            marX = round(random.randrange(0, lungime - size_of_block) / size_of_block) * size_of_block
            marY = round(random.randrange(0, inaltime - size_of_block) / size_of_block) * size_of_block
            snakeLenght+=1
        clock.tick(FPS)



    pygame.quit()

    quit()

gameLoop()