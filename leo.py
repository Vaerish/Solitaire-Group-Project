import pygame
import time
import random
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
black = (0,0,0)
white = (255, 255, 255) #color definitions
red = (200, 0, 0)
green = (0,200,0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

display_width = 1280
display_height = 720
crashed = False

card_width = 150

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Cool solitaire')

faceDown = pygame.image.load('Cards/PNG/gosnel.jpg')
faceDown = pygame.transform.scale(faceDown,(150,200))
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

def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitGame():
    print("Leaving")
    pygame.quit()
    quit()
    
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
    
# function will randomly generates the cards in desk array and place on the UI
# NOTE: should rezise or rescale the cards to make sure they can fix for all seven piles
def shuffle(x,y):
        for pile in range(100,1100,200):
                cardDis(pile,y)
        pygame.display.update()
                
        
        
#if you want to actually run game call game() at bottom as opposed to menu()
# I am working on a button to link between them though
def game():
    global crashed
    x = (display_width * 0.25)
    y = (display_height * .5)
    beginning = True
    click = True
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        ###########################################################################
        # this function uses to create a button to shuffering the cards
        # It is used for testing purpose but could be use in the game
        # when the player need refresh the cards from Draw Pile or restart the game
        # #########################################################################     
        if(pygame.mouse.get_pressed()[0]):
                if(pygame.mouse.get_pos()[0]>=700 
                        and pygame.mouse.get_pos()[0]<=800 
                        and pygame.mouse.get_pos()[1]>=0
                        and pygame.mouse.get_pos()[1]<=100):
                        button("Refresh",700,0,100,100,white,white,shuffle(x,y))
                        print(pygame.mouse.get_pos()[0])
                        print(pygame.mouse.get_pos()[1])
                        pygame.display.update()
        gameDisplay.fill(green)

        #initilizes the button and cards, the button doesn't have function
        # at beginning
        if (beginning == True):
                button("Refresh",700,0,100,100,white,bright_red,shuffle(x,y))         
                beginning = False
                pygame.display.update() 
        clock.tick(15)

def menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Solitaire The Best!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        msg = "Go"
        button(msg, 150, 450, 100, 50, green, bright_green, game)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitGame)
        
        mouse = pygame.mouse.get_pos()
        
        pygame.display.update()
        clock.tick(15)
                                  
clock = pygame.time.Clock()

def cardDis(x,y):
        randomCard = random.randint(0,len(deck)-1)
        gameDisplay.blit(deck[randomCard], (x, y))





menu()
pygame.quit()
quit()
