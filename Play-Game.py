import pygame
import time
import random
import math
import Tanks
import slither

from pygame.locals import *


pygame.init()
white = (255,255,255)
red = (200,0,0)
light_red = (255,0,0)

green = (0,155,0)
light_green = (0,255,0)

blue = (0,0,255)
black = (0,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

display_width = 800
display_height = 600





gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game Box') #title for the project

clock = pygame.time.Clock()
block_size = 20
FPS = 10


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

    
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
         textSurface = medfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)    
    
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, button_width, button_height, size= "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(button_width/2)), buttony+(button_height/2))
    gameDisplay.blit(textSurf, textRect)



def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurf, textRect = text_objects(msg ,color,size)
    textRect.center = (display_width/ 2),(display_height / 2)+y_displace
    gameDisplay.blit(textSurf,textRect)

def game_controls():
    
    gcont = True

    while gcont:
        for event in  pygame.event.get():  
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        
        gameDisplay.fill(white)
        message_to_screen("ABOUT",
                          green,
                          -100,
                          "large")
        message_to_screen("Game Box is collection of 2 Games",
                          black,
                          -30,
                          "small")
        message_to_screen("Clash Of Tank",
                          black,
                          10,
                          "small")
        
        message_to_screen("Slither Snake Game",
                          black,
                          50,"small")
        message_to_screen("Developed by : Naveen Kumar Verma",
                          black,
                          90,"small")

        button("Snake",50,500,100,50,green ,light_green,action= "snake")
        button("Tank",350,500,100,50,green ,light_green,action= "tanks")
        button("Quit",650,500,100,50, red, light_red,action = "quit")
        
        pygame.display.update()

        clock.tick(15)


def button(text, x, y, width, height, inactive_color, active_color, action = "None"):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + width > cur[0] > x and y + height > cur[1] > y:

        pygame.draw.rect(gameDisplay, active_color,(x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                quit()

            if action == "controls":
                game_controls()
                
            if action == "snake":
                pygame.display.set_caption('Slither')
                slither.game_intro()

            if action == "easy":
                easyGameLoop()
            if action == "hard":
                gameLoop()
            if action == "tanks":
                pygame.display.set_caption('Tanks')
                Tanks.game_intro()
    else:
        pygame.draw.rect(gameDisplay, inactive_color,(x, y, width, height))

    text_to_button(text,black,x,y,width,height)

def main_game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()        
        gameDisplay.fill(white)
        message_to_screen("Welcome to GameBox",
                          green,
                          -100,
                          "large")
        message_to_screen("The Clash Of Tanks",
                          black,
                          0,
                          "small")
        message_to_screen("Silther : the snake GAme",
                          black,
                          40,
                          "small")

        button("Snake",50,500,100,50,green ,light_green,action= "snake")
        button("Tank",250,500,100,50,green ,light_green,action= "tanks")
        button("ABOUT",450,500,100,50, yellow, light_yellow,action = "controls")
        button("QUIT",650,500,100,50, red, light_red,action = "quit")
        pygame.display.update()
        clock.tick(15)

main_game_intro()


