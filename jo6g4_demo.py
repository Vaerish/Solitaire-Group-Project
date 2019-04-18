import pygame
import time
import random
import sys
from pygame.locals import *

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)  # color definitions
red = (200, 0, 0)
green = (0, 200, 0)


cyan = (0,238,238)


bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

display_width = 1280
display_height = 720
crashed = False

card_width = 75
card_height = 100

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Cool solitaire')

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



# card_directory = {}
#
# card = pygame.image.load('Cards/PNG/AD.png').convert()
# card_directory["ace_diamonds"] = card
# card = pygame.image.load('Cards/PNG/AC.png').convert()
# card_directory["ace_clubs"] = card
# card = pygame.image.load('Cards/PNG/AH.png').convert()
# card_directory["ace_hearts"] = card
#
# #######################################################
# card = pygame.image.load('Cards/PNG/AS.png').convert()
# card_directory["ace_spades"] = card
# card = pygame.image.load('Cards/PNG/6D.png').convert()
# card_directory["6_diamond"] = card
# card = pygame.image.load('Cards/PNG/6C.png').convert()
# card_directory["6_club"] = card


# heart6 = pygame.image.load('Cards/PNG/6H.png')
# heart6 = pygame.transform.scale(heart6, (card_width, card_height))
# spade6 = pygame.image.load('Cards/PNG/6S.png')
# spade6 = pygame.transform.scale(spade6, (card_width, card_height))
# diamond7 = pygame.image.load('Cards/PNG/7D.png')
# diamond7 = pygame.transform.scale(diamond7, (card_width, card_height))
# club7 = pygame.image.load('Cards/PNG/7C.png')
# club7 = pygame.transform.scale(club7, (card_width, card_height))
# heart7 = pygame.image.load('Cards/PNG/7H.png')
# heart7 = pygame.transform.scale(heart7, (card_width, card_height))
# spade7 = pygame.image.load('Cards/PNG/7S.png')
# spade7 = pygame.transform.scale(spade7, (card_width, card_height))
# diamond8 = pygame.image.load('Cards/PNG/8D.png')
# diamond8 = pygame.transform.scale(diamond8, (card_width, card_height))
# club8 = pygame.image.load('Cards/PNG/8C.png')
# club8 = pygame.transform.scale(club8, (card_width, card_height))
# heart8 = pygame.image.load('Cards/PNG/8H.png')
# heart8 = pygame.transform.scale(heart8, (card_width, card_height))
# spade8 = pygame.image.load('Cards/PNG/8S.png')
# spade8 = pygame.transform.scale(spade8, (card_width, card_height))
# diamond9 = pygame.image.load('Cards/PNG/9D.png')
# diamond9 = pygame.transform.scale(diamond9, (card_width, card_height))
# club9 = pygame.image.load('Cards/PNG/9C.png')
# club9 = pygame.transform.scale(club9, (card_width, card_height))
# heart9 = pygame.image.load('Cards/PNG/9H.png')
# heart9 = pygame.transform.scale(heart9, (card_width, card_height))
# spade9 = pygame.image.load('Cards/PNG/9S.png')
# spade9 = pygame.transform.scale(spade9, (card_width, card_height))
# diamond10 = pygame.image.load('Cards/PNG/10D.png')
# diamond10 = pygame.transform.scale(diamond10, (150, card_height))
# club10 = pygame.image.load('Cards/PNG/10C.png')
# club10 = pygame.transform.scale(club10, (card_width, card_height))
# heart10 = pygame.image.load('Cards/PNG/10H.png')
# heart10 = pygame.transform.scale(heart10, (card_width, card_height))
# spade10 = pygame.image.load('Cards/PNG/10S.png')
# spade10 = pygame.transform.scale(spade10, (card_width, card_height))
# diamondJ = pygame.image.load('Cards/PNG/JD.png')
# diamondJ = pygame.transform.scale(diamondJ, (card_width, card_height))
# clubJ = pygame.image.load('Cards/PNG/JC.png')
# clubJ = pygame.transform.scale(clubJ, (card_width, card_height))
# heartJ = pygame.image.load('Cards/PNG/JH.png')
# heartJ = pygame.transform.scale(heartJ, (card_width, card_height))
# spadeJ = pygame.image.load('Cards/PNG/JS.png')
# spadeJ = pygame.transform.scale(spadeJ, (card_width, card_height))
# diamondQ = pygame.image.load('Cards/PNG/QD.png')
# diamondQ = pygame.transform.scale(diamondQ, (card_width, card_height))
# clubQ = pygame.image.load('Cards/PNG/QC.png')
# clubQ = pygame.transform.scale(clubQ, (card_width, card_height))
# heartQ = pygame.image.load('Cards/PNG/QH.png')
# heartQ = pygame.transform.scale(heartQ, (card_width, card_height))
# spadeQ = pygame.image.load('Cards/PNG/QS.png')
# spadeQ = pygame.transform.scale(spadeQ, (card_width, card_height))
# diamondK = pygame.image.load('Cards/PNG/KD.png')
# diamondK = pygame.transform.scale(diamondK, (card_width, card_height))
# clubK = pygame.image.load('Cards/PNG/KC.png')
# clubK = pygame.transform.scale(clubK, (card_width, card_height))
# heartK = pygame.image.load('Cards/PNG/KH.png')
# heartK = pygame.transform.scale(heartK, (card_width, card_height))
# spadeK = pygame.image.load('Cards/PNG/KS.png')
# spadeK = pygame.transform.scale(spadeK, (card_width, card_height))





deck = [diamondA, clubA, heartA, spadeA, diamond6, club6, heart6, spade6, diamond7, club7, heart7, spade7, diamond8,
        club8, heart8, spade8,
        diamond9, club9, heart9, spade9, diamond10, club10, heart10, spade10, diamondJ, clubJ, heartJ,
        spadeJ, diamondQ, clubQ, heartQ, spadeQ, diamondK, clubK, heartK, spadeK]


def __init__(self, x, y):
    self.cards = []
    self.rect = pygame.Rect(x, y, 71, 96)

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
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
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    return


# if you want to actually run game call game() at bottom as opposed to menu()
# I am working on a button to link between them though
def game():
    global crashed
    x = (display_width * 0.25)
    y = (display_height * .5)
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        gameDisplay.fill(white)
        cardDis(x, y)
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
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Solitaire The Best!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        msg = "Go"
        button(msg, 150, 450, 100, 50, green, bright_green, game)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitGame)
        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(15)


clock = pygame.time.Clock()

def layout(screen,deck):

    outlineCard = pygame.image.load('Cards/PNG/deck_background.png')
    outlineCard = pygame.transform.scale(outlineCard, (80, 100))
    screen.blit(outlineCard, (20, 20))
    # screen.blit(outlineCard, (100, 20))
    screen.blit(outlineCard, (180, 20))
    screen.blit(outlineCard, (360, 20))

    # waste
    screen.blit(outlineCard, (560, 20))

    backofcardRed = pygame.image.load('Cards/PNG/red_back.png')
    backofcardRed = pygame.transform.scale(backofcardRed, (80, 100))
    backofcardPurple = pygame.image.load('Cards/PNG/purple_back.png')
    backofcardPurple = pygame.transform.scale(backofcardPurple, (80, 100))
    backofcardYellow = pygame.image.load('Cards/PNG/yellow_back.png')
    backofcardYellow = pygame.transform.scale(backofcardYellow, (80, 100))


    screen.blit(backofcardRed, (20, 50))
    mouseX, mouseY = pygame.mouse.get_pos()
    # screen.blit(backofcardRed, (mouseX - 50, mouseY - 50))
    screen.blit(backofcardPurple, (180, 50))
    screen.blit(backofcardYellow, (360, 50))

    deckLen = len(deck)
    # for i in range(1, deckLen):
    #     clock.tick(60)
    #     screen.blit(deck[i], (20, 20))
    #     pygame.display.flip()

    running = True
    while running :
        for event in pygame.event.get():
            for i in range(1,deckLen):
                pygame.display.flip()
                clock.tick(10)
                screen.blit(deck[i],(20,20))
                pygame.display.update()
            if event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                # screen.blit(backofcardRed, (mouseX - 50, mouseY - 50))
                pygame.display.flip()
            elif event.type == K_ESCAPE:
                pygame.quit()
                running = False

        # screen.blit(backofcardPurple, (mouseX, mouseY))
        # screen.blit(backofcardYellow, (mouseX, mouseY))
    # screen.blit(backofcardRed, (mouseX-50, mouseY-50))
    # clock.tick(60)
    pygame.display.flip()



         # screen.blit(backofcardPurple, (mouseX, mouseY))
         # screen.blit(backofcardYellow, (mouseX, mouseY))


def cardDis(x, y):
    layout(gameDisplay,deck)










# def drawCards(self, screen, entireDeck):
#     pygame.draw.rect(screen, black, [self.rect.left, self.rect.top, 71, 96], 2)
#     j = self.y
#     if len(self.hidden) > 0:
#         for i in self.hidden:
#             pygame.draw.rect(screen, red, [self.rect.left, i, 71, 96])
#             pygame.draw.rect(screen, black, [self.rect.left, j, 71, 96], 2)
#             j+=37
#
#     if len(self.cards) > 0:
#         for i in self.cards:
#             screen.blit(entireDeck[i],[self.rect.left,j])
#             j+=37
#
# def drawMovedCards(self, screen, entireDeck):
#     if self.moved:
#         position = pygame.mouse.get_pos()
#         xPos = position[0] - self.c[0]
#         yPos = position[1] - self.c[1]
#         for i in self.moved_card:
#             screen.blit(entireDeck[i], [xPos , yPos])
#             yPos += 10 # testing number
#
# def addCards(self, card):
#     if len(self.cards) > 0 or len(self.hidden) > 0:
#         for j in range(len(card)):
#             self.rect.top += 2 #this is just a test
#     else:
#         for j in range(len(card)):
#             if j > 0:
#                 self.rect.top += 4 #again, just a test
#     self.cards.extend(card)
#
#
#
#
#
#
# def shuffle(deck):
#     x = []
#     length = len(deck)
#     for j in range(length):
#         if len(deck) > 1:
#             q = random.choice(deck)
#             x.append(q)
#             deck.remove(q)
#         else:
#             q = deck.pop()
#             x.append(q)
#
#     return x


menu()
pygame.quit()
quit()


