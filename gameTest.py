import pygame
import time
import random

pygame.init()

black = (0,0,0)
white = (255, 255, 255) #color definitions
gray = (83, 85, 83)
red = (153, 18, 18)
green = (47, 110, 41)

bright_red = (46, 7, 7)
bright_green = (16, 34, 14)

display_width = 1280
display_height = 720
crashed = False

card_width = 150
card_length = 200

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Cool solitaire')

RED = ["D", "H"]
BLACK = ["S", "C"]

SUITS = ["D", "S", "C", "H"]
FACES = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# It's, ya know, a card.  Has all the member variables needed for rule checking and such
class Card:
    suit = ""
    face = ""
    color = ""
    number = False
    image = None

    # Constructor, takes a face and a suit
    def __init__(self, face, suit):
        self.suit = suit
        self.face = face
        self.image = pygame.image.load("Cards/PNG/{}{}.png".format(self.face, self.suit))
        self.image = pygame.transform.scale(self.image, (card_width,card_length))
        self.color = "R" if self.suit in RED else "B"
        self.number = self.face.isdigit()
    
    def __str__(self):
        return "{}{}".format(self.face, self.suit)

    def __repr__(self):
        return "{}{}".format(self.face, self.suit)

# A stack of cards.  The "top" of the stack is at the end of the list
class CardStack:
    # a list of Cards
    __cards = []
    # keeps track of which cards have been "touched".  This means they have been
    #   moved by the user, and will be evaluated by the rules.  This is an index
    #   of __cards, where everything after it has been touched
    __touched = 0

    # Class constructor.  Takes a list of Cards, and whether they have been touched
    def __init__(self, stack, touched = False):
        self.__cards = stack
        self.__touched = 0 if touched else len(self.__cards) - 1
    
    def __add__(self, other):
        self.append(other)
    
    def __str__(self):
        return str(self.__cards)

    def __repr__(self):
        return str(self.__cards)
    
    # Returns the stack as a list of Cards
    def stack(self):
        return self.__cards

    # Adds a CardStack to this one.  Note that this assumes that all added
    #   Cards are considered "touched"
    def append(self, stack):
        self.__cards += stack.stack()
    
    # Removes a number of Cards from the stack and returns them as a CardStack
    def remove(self, numCards):
        removed = CardStack(self.__cards[-1*numCards:], True)
        self.__cards = self.__cards[:-1*numCards]
        if self.__touched > len(self.__cards):
            self.__touched = len(self.__cards) - 1
        return removed
    
    # Returns __touched
    def touched(self):
        return self.__touched



#faceDown = pygame.image.load('Cards/PNG/gosnel.jpg')
#faceDown = pygame.transform.scale(faceDown,(card_width,card_length))

# generates a complete list of Cards
def generateDeck():
    deck = []
    for suit in SUITS:
        for face in FACES:
            card = Card(face, suit)
            deck.append(card)
    return deck



deck = generateDeck()


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


# function will randomly generates the cards in desk array and place on the UI
# NOTE: should rezise or rescale the cards to make sure they can fix for all seven piles
def shuffle():
    x = (display_width * 0.25)
    y = (display_height * .5)
    for pile in range(100, 1100, 200):
        cardDis(pile, y)
    pygame.display.update()


# if you want to actually run game call game() at bottom as opposed to menu()
# I am working on a button to link between them though
def game():
    mouse = pygame.mouse.get_pos()
    global crashed
    x = (display_width * 0.25)
    y = (display_height * .5)
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

        button("Refresh", 700, 0, 100, 100, white, gray, shuffle)
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
        gameDisplay.fill(gray)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Solitaire!", largeText)
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
    #outlineCard = pygame.image.load('Cards/PNG/gosnel.jpg')
    # screen.blit(outlineCard, (20, 20))
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
    gameDisplay.blit(deck[randomCard].image, (x, y))


menu()
pygame.quit()
quit()

