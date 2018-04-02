import pygame
import time
import random
import math


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



snakehead = pygame.image.load("snakehead.png")
icon = pygame.image.load("snakehead.png")
apple = pygame.image.load("apple.png")

pygame.display.set_icon(icon)#To set icon
pygame.display.update() #To update the frame


clock = pygame.time.Clock()
block_size = 20
FPS = 10

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def hitMusic():
    pygame.mixer.music.load("hit.wav")
    pygame.mixer.music.play()
    
def eatMusic():
    pygame.mixer.music.load("beep.wav")
    pygame.mixer.music.play()
    
def wall():
    pygame.draw.rect(gameDisplay, yellow,[210,200,block_size*20,block_size+10])
    pygame.draw.rect(gameDisplay, yellow,[210,400,block_size*20,block_size+10])
    pygame.draw.rect(gameDisplay, yellow,[0,0,display_width,block_size])#upper boundary
    pygame.draw.rect(gameDisplay, yellow,[0,0,block_size,display_height])#left boundary
    pygame.draw.rect(gameDisplay, yellow,[display_width-block_size,0,block_size,display_height])#right boundary
    pygame.draw.rect(gameDisplay, yellow,[0,display_height-block_size,display_width,block_size])#bottom boundary
    
    
    pygame.display.update()



def score(score):
  
    Score_text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(Score_text, [0,0])
    
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



def snake(block_size, snakelist):
    if direction == "right":
       head = pygame.transform.rotate(snakehead,270)
    if direction == "left":
       head = pygame.transform.rotate(snakehead,90)
    if direction == "up":
       head = snakehead
    if direction == "down":
       head = pygame.transform.rotate(snakehead,180)
       
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green,[XnY[0],XnY[1],block_size,block_size])
        

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
        message_to_screen("CONTROLS",
                          green,
                          -100,
                          "large")
        message_to_screen("To Move Left, Right, Up, Down  :Use Arrow Keys",
                          black,
                          -30,
                          "small")
        message_to_screen("If You Run Over The Boundaries You will Die",
                          black,
                          10,
                          "small")
        
        message_to_screen("The Mode You Choose that is EASY or HARD ",
                          black,
                          50,"small")
        message_to_screen("The Complexity Will Be According To It Only",
                          black,
                          90,"small")
        message_to_screen("Pause : P",
                          black,
                          130,"small")     

        button("EASY",51,450,100,50,green ,light_green,action= "easy")
        button("HARD",351,450,100,50,green ,light_green,action= "hard")
        button("QUIT",651,450,100,50, red, light_red,action = "quit")
        
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
            if action == "play":
                gameMode()
            if action == "main" or action == "snake":
                game_intro()

            if action == "easy":
                easyGameLoop()
            if action == "hard":
                gameLoop()
            if action == "tanks":
                Tanks.game_intro()
    else:
        pygame.draw.rect(gameDisplay, inactive_color,(x, y, width, height))

    text_to_button(text,black,x,y,width,height)
    
def pause():
    paused = True
    message_to_screen("Pause",
                      black,
                      -100,
                      size="large")
    
    message_to_screen("Press C to continue or Q to Quit",
                      black,
                      25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    paused = False

                elif event.key == K_q:
                    pygame.quit()
                    quit()



        clock.tick(5)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        
        gameDisplay.fill(white)
        message_to_screen("Slither : Snake Game",
                          green,
                          -100,
                          "large")
        message_to_screen("Objective of the Game is to eat the RED Apples",
                          black,
                          0,
                          "small")
        message_to_screen("The more Apples you eat ,the LONGER you get",
                          black,
                          40,
                          "small")
        

        button("EASY",51,450,100,50,green ,light_green,action= "easy")
        button("HARD",251,450,100,50,green ,light_green,action= "hard")
        button("controls",451,450,100,50, yellow, light_yellow,action = "controls")
        button("QUIT",651,450,100,50, red, light_red,action = "quit")
        pygame.display.update()
        clock.tick(15)



def easyGameLoop():
    global direction
    global FPS
    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    randAppleX = round(random.randrange(0,display_width-block_size)) 
    randAppleY = round(random.randrange(0,display_height-block_size))

    
    while not gameExit:
        if gameOver == True:
            FPS = 10

            message_to_screen("Game Over",
                              red,
                              y_displace=-50,
                              size="large")
            message_to_screen("Press C to Play and Q to Quit ",
                              black,
                              50,
                              size="medium")
            pygame.display.update()
        while gameOver == True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

                if event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == K_c:
                        easyGameLoop()



        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    direction= "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == K_d:
                    direction= "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == K_UP or event.key == K_w:
                    direction= "up"
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == K_DOWN or event.key == K_s:
                    direction= "down"
                    lead_x_change = 0
                    lead_y_change = block_size
                    


                elif event.key == K_p:
                    pause()

        lead_x+=lead_x_change
        lead_y+=lead_y_change
        lead_x = lead_x%display_width
        lead_y = lead_y%display_height
        gameDisplay.fill(white)

        AppleThickness = 20
        
        gameDisplay.blit(apple,(randAppleX, randAppleY))




        
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength :
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeLength:
                gameOver = True
                
        snake(block_size, snakeList)

        score(snakeLength-1)
        pygame.display.update() #To update the frame
        
        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness or lead_x + block_size >= randAppleX and lead_x + block_size <= randAppleX + AppleThickness:
             if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness or lead_y + block_size >= randAppleY and lead_y + block_size <= randAppleY + AppleThickness:
                 eatMusic()
                 randAppleX = round(random.randrange(0,display_width-block_size))
                 randAppleY = round(random.randrange(1,display_height-block_size))
                 snakeLength+=1
        
        
        clock.tick(FPS)        



    message_to_screen("You lose",red,-100,"medium")
    message_to_screen("Your Score is "+str(snakeLength-1),green,-50,"medium")

    pygame.display.update() #To update the frame
    time.sleep(1)
    pygame.quit()
    quit()






def gameLoop():
    global direction
    global FPS
    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    randAppleX = round(random.randrange(block_size*2+10,display_width-block_size*2-10)) 
    randAppleY = round(random.randrange(block_size*2+10,display_height-block_size*2-10))
    

    if 200 <= randAppleX <=620 and (190 <= randAppleY <= 240 or 390 <= randAppleY <= 440):
        gameLoop()
    
    while not gameExit:
        if gameOver == True:
            FPS = 10
            
            message_to_screen("Game Over",
                              red,
                              y_displace=-50,
                              size="large")
            message_to_screen("Press C to Play and Q to Quit ",
                              black,
                              50,
                              size="medium")
            pygame.display.update()
        while gameOver == True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

                if event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == K_c:
                        gameLoop()



        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    direction= "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == K_d:
                    direction= "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == K_UP or event.key == K_w:
                    direction= "up"
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == K_DOWN or event.key == K_s:
                    direction= "down"
                    lead_x_change = 0
                    lead_y_change = block_size
                    


                elif event.key == K_p:
                    pause()

        if display_width-21>=lead_x>=20 and display_height-21>=lead_y>=20:
            if (600 >= lead_x >= 200 and (220 >= lead_y >= 200 or 420 >= lead_y >= 400)) :
                hitMusic()
                gameOver = True
            else :
                gameOver = False
        else:
            hitMusic()
            gameOver = True

        lead_x+=lead_x_change
        lead_y+=lead_y_change
        
        gameDisplay.fill(white)

        AppleThickness = 20
        wall()
        
        gameDisplay.blit(apple,(randAppleX, randAppleY))




        
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength :
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeLength:
                gameOver = True
                
        snake(block_size, snakeList)

        score(snakeLength-1)
        pygame.display.update() #To update the frame

        
        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness or lead_x + block_size >= randAppleX and lead_x + block_size <= randAppleX + AppleThickness:
             if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness or lead_y + block_size >= randAppleY and lead_y + block_size <= randAppleY + AppleThickness:
                 eatMusic()
                 randAppleX,randAppleY = ApplePos()
                 


                 if 200 <= randAppleX <=620 and (190 <= randAppleY <= 240 or 390 <= randAppleY <= 440):
                     
                     randAppleX,randAppleY = ApplePos()

                 snakeLength+=1
        
        
        clock.tick(FPS)        



    message_to_screen("You lose",red,-100,"medium")
    message_to_screen("Your Score is "+str(snakeLength-1),green,-50,"medium")

    pygame.display.update() #To update the frame
    time.sleep(1)
    pygame.quit()
    quit()

def ApplePos():
    randAppleX = round(random.randrange(block_size*2+10,display_width-block_size*2-10)) 
    randAppleY = round(random.randrange(block_size*2+10,display_height-block_size*2-10))
    return randAppleX,randAppleY



