#Maddie's Schtuff

import pygame
import time
import random
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

black = (0,0,0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0,200,0)
cyan = (0,238,238)
lavender = (192, 186, 253)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

#init window
display_width = 1280
display_height = 720
crashed = False

#init card sizes
#need to be pretty small with 9 stacks
card_width = 100
card_height = 133

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('does anyone really read this part?')

diamondA = pygame.image.load('Cards/PNG/AD.png')
diamondA = pygame.transform.scale(diamondA, (card_width, card_height))
clubA = pygame.image.load('Cards/PNG/AC.png')
clubA = pygame.transform.scale(clubA, (card_width, card_height))
heartA = pygame.image.load('Cards/PNG/AH.png')
heartA = pygame.transform.scale(heartA, (card_width, card_height))
spadeA = pygame.image.load('Cards/PNG/AS.png')
spadeA = pygame.transform.scale(spadeA, (card_width, card_height))
diamond6 = pygame.image.load('Cards/PNG/6D.png')
diamond6 = pygame.transform.scale(diamond6, (card_width, card_height))
club6 = pygame.image.load('Cards/PNG/6C.png')
club6 = pygame.transform.scale(club6, (card_width, card_height))
heart6 = pygame.image.load('Cards/PNG/6H.png')
heart6 = pygame.transform.scale(heart6, (card_width, card_height))
spade6 = pygame.image.load('Cards/PNG/6S.png')
spade6 = pygame.transform.scale(spade6, (card_width, card_height))
diamond7 = pygame.image.load('Cards/PNG/7D.png')
diamond7 = pygame.transform.scale(diamond7, (card_width, card_height))
club7 = pygame.image.load('Cards/PNG/7C.png')
club7 = pygame.transform.scale(club7, (card_width, card_height))
heart7 = pygame.image.load('Cards/PNG/7H.png')
heart7 = pygame.transform.scale(heart7, (card_width, card_height))
spade7 = pygame.image.load('Cards/PNG/7S.png')
spade7 = pygame.transform.scale(spade7, (card_width, card_height))
diamond8 = pygame.image.load('Cards/PNG/8D.png')
diamond8 = pygame.transform.scale(diamond8, (card_width, card_height))
club8 = pygame.image.load('Cards/PNG/8C.png')
club8 = pygame.transform.scale(club8, (card_width, card_height))
heart8 = pygame.image.load('Cards/PNG/8H.png')
heart8 = pygame.transform.scale(heart8, (card_width, card_height))
spade8 = pygame.image.load('Cards/PNG/8S.png')
spade8 = pygame.transform.scale(spade8, (card_width, card_height))
diamond9 = pygame.image.load('Cards/PNG/9D.png')
diamond9 = pygame.transform.scale(diamond9, (card_width, card_height))
club9 = pygame.image.load('Cards/PNG/9C.png')
club9 = pygame.transform.scale(club9, (card_width, card_height))
heart9 = pygame.image.load('Cards/PNG/9H.png')
heart9 = pygame.transform.scale(heart9, (card_width, card_height))
spade9 = pygame.image.load('Cards/PNG/9S.png')
spade9 = pygame.transform.scale(spade9, (card_width, card_height))
diamond10 = pygame.image.load('Cards/PNG/10D.png')
diamond10 = pygame.transform.scale(diamond10, (card_width, card_height))
club10 = pygame.image.load('Cards/PNG/10C.png')
club10 = pygame.transform.scale(club10, (card_width, card_height))
heart10 = pygame.image.load('Cards/PNG/10H.png')
heart10 = pygame.transform.scale(heart10, (card_width, card_height))
spade10 = pygame.image.load('Cards/PNG/10S.png')
spade10 = pygame.transform.scale(spade10, (card_width, card_height))
diamondJ = pygame.image.load('Cards/PNG/JD.png')
diamondJ = pygame.transform.scale(diamondJ, (card_width, card_height))
clubJ = pygame.image.load('Cards/PNG/JC.png')
clubJ = pygame.transform.scale(clubJ, (card_width, card_height))
heartJ = pygame.image.load('Cards/PNG/JH.png')
heartJ = pygame.transform.scale(heartJ, (card_width, card_height))
spadeJ = pygame.image.load('Cards/PNG/JS.png')
spadeJ = pygame.transform.scale(spadeJ, (card_width, card_height))
diamondQ = pygame.image.load('Cards/PNG/QD.png')
diamondQ = pygame.transform.scale(diamondQ, (card_width, card_height))
clubQ = pygame.image.load('Cards/PNG/QC.png')
clubQ = pygame.transform.scale(clubQ, (card_width, card_height))
heartQ = pygame.image.load('Cards/PNG/QH.png')
heartQ = pygame.transform.scale(heartQ, (card_width, card_height))
spadeQ = pygame.image.load('Cards/PNG/QS.png')
spadeQ = pygame.transform.scale(spadeQ, (card_width, card_height))
diamondK = pygame.image.load('Cards/PNG/KD.png')
diamondK = pygame.transform.scale(diamondK, (card_width, card_height))
clubK = pygame.image.load('Cards/PNG/KC.png')
clubK = pygame.transform.scale(clubK, (card_width, card_height))
heartK = pygame.image.load('Cards/PNG/KH.png')
heartK = pygame.transform.scale(heartK, (card_width, card_height))
spadeK = pygame.image.load('Cards/PNG/KS.png')
spadeK = pygame.transform.scale(spadeK, (card_width, card_height))

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

def quitInGame():
    print("Thanks for playing")
    pygame.quit
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
    

def initCards():
    x = (display_width * 0.1)
    y = (display_height * .4)
    for pile in range(100, 1000, 122):
      cardDis(pile, (y - 200))
      cardDis(pile, (y - 150))
      cardDis(pile, (y - 100))
      cardDis(pile, (y - 50))
      cardDis(pile, (y))
    pygame.display.update()
    
# function will randomly generates the cards in desk array and place on the UI
# NOTE: should rezise or rescale the cards to make sure they can fix for all seven piles
def shuffle():
    x = (display_width * 0.1)
    y = (display_height * .4)
    for pile in range(100, 1000, 122):
        cardDis(pile, y)
    pygame.display.update()


# if you want to actually run game call game() at bottom as opposed to menu()
# I am working on a button to link between them though
def game():
    mouse = pygame.mouse.get_pos()
    global crashed
    x = (display_width * 0.25)
    y = (display_height * .5)
    initCards()
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

        button("Refresh", 700, 0, 100, 100, white, lavender, shuffle)
        pygame.display.update()
        clock.tick(15)


def menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(lavender)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Solitaire! Nice!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        msg = "Go"
        button(msg, 150, 450, 200, 50, green, bright_green, game)
        button("Quit", 900, 450, 200, 50, red, bright_red, quitGame)

        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(15)


clock = pygame.time.Clock()


def layout(screen):
    outlineCard = pygame.image.load('Cards/PNG/gosnel.jpg')
    screen.blit(outlineCard, (20, 20))
    # screen.blit(outlineCard, (100, 20))
    # screen.blit(outlineCard, (180, 20))
    # screen.blit(outlineCard, (260, 20))
    #
    # # waste
    # screen.blit(outlineCard, (560, 20))
    #
    # backofcardRed = pygame.image.load('Cards/PNG/red_back.png')
    # backofcardRed = pygame.transform.scale(backofcardRed, (140, 140))
    # backofcardPurple = pygame.image.load('Cards/PNG/purple_back.png')
    # backofcardPurple = pygame.transform.scale(backofcardPurple, (140, 140))
    # backofcardYellow = pygame.image.load('Cards/PNG/yellow_back.png')
    # backofcardYellow = pygame.transform.scale(backofcardYellow, (140, 140))
    #
    # screen.blit(backofcardRed, (725, 20))
    # screen.blit(backofcardPurple, (750, 20))
    # screen.blit(backofcardYellow, (780, 20))
    screen.fill(bright_green)


def cardDis(x, y):
    randomCard = random.randint(0, len(deck) - 1)
    gameDisplay.blit(deck[randomCard], (x, y))


menu()
pygame.quit()
quit()