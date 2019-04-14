import pygame
import time
import random
from pygame.locals import *
pygame.init()

black = (0,0,0)
white = (255, 255, 255) #color definitions
red = (255, 0, 0)
display_width = 1280
display_height = 720
crashed = False

card_width = 150

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Cool solitaire')

diamondA = pygame.image.load('Cards/PNG/AD.png')
diamondA = pygame.transform.scale(diamondA, (150, 200))
clubA = pygame.image.load('Cards/PNG/AC.png')
clubA = pygame.transform.scale(clubA, (150, 200))
heartA = pygame.image.load('Cards/PNG/AH.png')
heartA = pygame.transform.scale(heartA, (150, 200))
spadeA = pygame.image.load('Cards/PNG/AS.png')
spadeA = pygame.transform.scale(spadeA, (150, 200))
diamond6 = pygame.image.load('Cards/PNG/6D.png')
diamond6 = pygame.transform.scale(diamond6, (150, 200))
club6 = pygame.image.load('Cards/PNG/6C.png')
club6  = pygame.transform.scale(club6 , (150, 200))
heart6 = pygame.image.load('Cards/PNG/6H.png')
heart6  = pygame.transform.scale(heart6, (150, 200))
spade6 = pygame.image.load('Cards/PNG/6S.png')
spade6  = pygame.transform.scale(spade6, (150, 200))
diamond7 = pygame.image.load('Cards/PNG/7D.png')
diamond7 = pygame.transform.scale(diamond7, (150, 200))
club7 = pygame.image.load('Cards/PNG/7C.png')
club7 = pygame.transform.scale(club7, (150, 200))
heart7 = pygame.image.load('Cards/PNG/7H.png')
heart7 = pygame.transform.scale(heart7, (150, 200))
spade7 = pygame.image.load('Cards/PNG/7S.png')
spade7 = pygame.transform.scale(spade7, (150, 200))
diamond8 = pygame.image.load('Cards/PNG/8D.png')
diamond8 = pygame.transform.scale(diamond8, (150, 200))
club8 = pygame.image.load('Cards/PNG/8C.png')
club8 = pygame.transform.scale(club8, (150, 200))
heart8 = pygame.image.load('Cards/PNG/8H.png')
heart8 = pygame.transform.scale(heart8, (150, 200))
spade8 = pygame.image.load('Cards/PNG/8S.png')
spade8 = pygame.transform.scale(spade8, (150, 200))
diamond9 = pygame.image.load('Cards/PNG/9D.png')
diamond9 = pygame.transform.scale(diamond9, (150, 200))
club9 = pygame.image.load('Cards/PNG/9C.png')
club9 = pygame.transform.scale(club9, (150, 200))
heart9 = pygame.image.load('Cards/PNG/9H.png')
heart9 = pygame.transform.scale(heart9, (150, 200))
spade9 = pygame.image.load('Cards/PNG/9S.png')
spade9 = pygame.transform.scale(spade9, (150, 200))
diamond10 = pygame.image.load('Cards/PNG/10D.png')
diamond10 = pygame.transform.scale(diamond10, (150, 200))
club10 = pygame.image.load('Cards/PNG/10C.png')
club10 = pygame.transform.scale(club10, (150, 200))
heart10 = pygame.image.load('Cards/PNG/10H.png')
heart10 = pygame.transform.scale(heart10, (150, 200))
spade10 = pygame.image.load('Cards/PNG/10S.png')
spade10 = pygame.transform.scale(spade10, (150, 200))
diamondJ = pygame.image.load('Cards/PNG/JD.png')
diamondJ = pygame.transform.scale(diamondJ, (150, 200))
clubJ = pygame.image.load('Cards/PNG/JC.png')
clubJ = pygame.transform.scale(clubJ, (150, 200))
heartJ = pygame.image.load('Cards/PNG/JH.png')
heartJ = pygame.transform.scale(heartJ, (150, 200))
spadeJ = pygame.image.load('Cards/PNG/JS.png')
spadeJ = pygame.transform.scale(spadeJ, (150, 200))
diamondQ = pygame.image.load('Cards/PNG/QD.png')
diamondQ = pygame.transform.scale(diamondQ, (150, 200))
clubQ = pygame.image.load('Cards/PNG/QC.png')
clubQ = pygame.transform.scale(clubQ, (150, 200))
heartQ = pygame.image.load('Cards/PNG/QH.png')
heartQ = pygame.transform.scale(heartQ, (150, 200))
spadeQ = pygame.image.load('Cards/PNG/QS.png')
spadeQ = pygame.transform.scale(spadeQ, (150, 200))
diamondK = pygame.image.load('Cards/PNG/KD.png')
diamondK = pygame.transform.scale(diamondK, (150, 200))
clubK = pygame.image.load('Cards/PNG/KC.png')
clubK = pygame.transform.scale(clubK, (150, 200))
heartK = pygame.image.load('Cards/PNG/KH.png')
heartK = pygame.transform.scale(heartK, (150, 200))
spadeK = pygame.image.load('Cards/PNG/KS.png')
spadeK = pygame.transform.scale(spadeK, (150, 200))

deck = [diamondA, clubA, heartA, spadeA, diamond6, club6, heart6, spade6, diamond7, club7, heart7, spade7, diamond8, club8, heart8, spade8,
        diamond9, club9, heart9, spade9, diamond10, club10, heart10, spade10, diamondJ, clubJ, heartJ,
        spadeJ, diamondQ, clubQ, heartQ, spadeQ, diamondK, clubK , heartK, spadeK, diamondA ]

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    return

#if you want to display this instead make it call game instead of menu I'm working on buttons to make a new files
def game():
    x = (display_width * 0.25)
    y = (display_height * .5)
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        gameDisplay.fill(white)
        cardDis(x,y)
        pygame.display.update()
        clock.tick(15)
def menu():
    global crashed
    thing_startx = 80
    thing_starty = 600
    thing_width = 300
    thing_height = 50
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        message_display('Fun Solitaire')
        pygame.display.update()
        clock.tick(15)
                                  
clock = pygame.time.Clock()

def cardDis(x,y):
    
    gameDisplay.blit(deck[0], (x, y))
    





menu()
pygame.quit()
quit()

