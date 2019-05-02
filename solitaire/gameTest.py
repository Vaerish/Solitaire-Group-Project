import pygame
import time
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)  # color definitions
gray = (83, 85, 83)
red = (153, 18, 18)
green = (47, 110, 41)
cyan = (0,238,238)

bright_red = (46, 7, 7)
bright_green = (16, 34, 14)

display_width = 1300
display_height = 720
crashed = False

card_width = 10
card_length = 130

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Cool solitaire')

RED = ["D", "H"]
BLACK = ["S", "C"]

SUITS = ["D", "S", "C", "H"]
FACES = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]

piles=[]

class Pile:   
    def __init__(self,cards,x,y):
            self.card = cards
            self.x = x
            self.y = y



# It's, ya know, a card.  Has all the member variables needed for rule checking and such
class Card:
    suit = ""
    face = ""
    color = ""
    # New change
    x = None
    y = None
    # Constructor, takes a face and a suit
    def __init__(self, face, suit):
        self.suit = suit
        self.face = face
        self.image = pygame.image.load("Cards/PNG/{}{}.png".format(self.face, self.suit))
        self.image = pygame.transform.scale(self.image, (card_width, card_length))
        self.color = "R" if self.suit in RED else "B"
        self.number = self.face.isdigit()

    def __str__(self):
        return "{}{}".format(self.face, self.suit)

    def __repr__(self):
        return "{}{}".format(self.face, self.suit)


# Recursively checks for validity, returns the longest valid CardStack
# This can be used for all aspects of game logic.  Here's how:
#   * Can we pick up this stack (or sub-stack)?:
#       If that stack and what this function returns when fed that stack are
#           the same length, yes
#   * Can we place this card stack here?
#       If this stack appended on the end of where we're trying to place it
#           is fed into this function, and the return value is longer than the
#           list we're trying to place, then we can
#   * Is this stack "done"?
#       If that stack and what this function returns when fed that stack are
#           the same length, yes
#   * Have we won the game?
#       If we have exactly 8 (not 9!) complete stacks and there is no card
#           in the free space, then yes
def validStack(stack, i=0):
    if len(stack) - i <= 1:
        return stack
    elif len(stack) - i == 2:
        if stack[0 + i].number:
            if not (stack[1 + i].number and int(stack[0 + i].face) - 1 == int(stack[1 + i].face) and not stack[
                                                                                                             0 + i].color ==
                                                                                                         stack[
                                                                                                             1 + i].color):
                del stack[:i + 1]
        else:
            if not (not stack[1 + i].number and stack[1 + i].face == stack[0 + i].face):
                del stack[:i + 1]
        return stack
    else:
        return validStack(validStack(stack[:-1], 0 + i) + stack[-1:], 1 + i)


# removes numCards number of cards from a stack, and returns them
def pickUp(stack, numCards):
    removed = stack[-1 * numCards:]
    del stack[-1 * numCards:]
    return removed


# faceDown = pygame.image.load('Cards/PNG/gosnel.jpg')
# faceDown = pygame.transform.scale(faceDown,(card_width,card_length))

# generates a complete list of Cards
def generateDeck():
    deck = []
    for suit in SUITS:
        for face in FACES:
            card = Card(face, suit)
            deck.append(card)
    return deck


deck = generateDeck()

test = [Card("K", "C"), Card("10", "H"), Card("9", "C"), Card("8", "D"), Card("K", "D"), Card("J", "D")]
print(validStack(test))


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


# function will randomly generates the cards in desk array and place on the UI
# NOTE: should rezise or rescale the cards to make sure they can fix for all seven piles
def shuffle():
    piles =[]
    x = (display_width * 0.25)
    y = (display_height * .5)
    for index in range(100, 1100, 200):
        # cardDis(index, y)
        piles.append(Pile(random.randint(0, len(deck) - 1),index,y))
    for pile in piles:
        gameDisplay.blit(deck[pile.card].image, (pile.x, pile.y))
        print(deck[pile.card])
    pygame.display.update()


# if you want to actually run game call game() at bottom as opposed to menu()
# I am working on a button to link between them though
def game():
    mouse = pygame.mouse.get_pos()
    layout(gameDisplay)
    # pygame.mixer.music.load("Elevator-music.mp3")
    # pygame.mixer.music.set_volume(0.5)
    # pygame.mixer.music.play(-1)
    global crashed
    x = (display_width * 0.25)
    y = (display_height * .5)
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.mixer.music.stop()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    mouse = pygame.mouse.get_pos()
        ###########################################################################
        # this function uses to create a button to shuffering the cards
        # It is used for testing purpose but could be use in the game
        # when the player need refresh the cards from Draw Pile or restart the game
        # #########################################################################

        button("Refresh", 700, 0, 100, 100, white, gray, shuffle)

        button("Leave Game", 1100, 0, 150, 100, cyan, red, quitInGame)
        pygame.display.update()
        clock.tick(5)


def rules():
    intro = True
    while intro:
        for event in pygame.event.get():
                # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(gray)
        button("return", 50, 100, 200, 50, red, bright_red, menuQ)
        ruleText = pygame.font.Font("freesansbold.ttf", 12)
        # create a text suface object,
        # on which text is drawn on it.
        TextSurf, TextRect = text_objects('Number cards are stacked by alternating color and decreasing value,',ruleText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('and can be moved together as a stack of any size. Face cards are stacked by suit ', ruleText)
        TextRect.center = ((display_width / 2), (display_height / 2) + 15)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('and in any order, and can also be moved as a stack. However, a completed stack of face cards ', ruleText)
        TextRect.center = ((display_width / 2), (display_height / 2) + 30)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('placed directly on the board will become immovable. To win, sort the dealt cards into four completed', ruleText)
        TextRect.center = ((display_width / 2), (display_height / 2) + 45)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects(' stacks of number cards and four complete stacks of face cards. The free cell in the corner can store a single card of any type.', ruleText)
        TextRect.center = ((display_width / 2), (display_height / 2) + 65)
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        clock.tick(15)

def menuQ():
    menu()


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
        button("Rules", 500, 450, 200, 50, white, white, rules)
        mouse = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(5)


clock = pygame.time.Clock()


def layout(screen):
    x = 150
    y = 210
    screen.fill(bright_green)
    outlineCard = pygame.image.load('Cards/PNG/deck_background.png')
    outlineCard = pygame.transform.scale(outlineCard, (x, y))
    screen.blit(outlineCard, (20, 20))
    screen.blit(outlineCard, (180, 20))
    screen.blit(outlineCard, (360, 20))

    screen.blit(outlineCard, (560, 20))
    backofcardRed = pygame.image.load('Cards/PNG/red_back.png')
    backofcardRed = pygame.transform.scale(backofcardRed, (150, 190))
    backofcardPurple = pygame.image.load('Cards/PNG/purple_back.png')
    backofcardPurple = pygame.transform.scale(backofcardPurple, (150, 190))
    backofcardYellow = pygame.image.load('Cards/PNG/yellow_back.png')
    backofcardYellow = pygame.transform.scale(backofcardYellow, (150, 190))

    screen.blit(backofcardRed, (20, 50))
    mouseX, mouseY = pygame.mouse.get_pos()
    # screen.blit(backofcardRed, (mouseX - 50, mouseY - 50))
    screen.blit(backofcardPurple, (180, 50))
    screen.blit(backofcardYellow, (360, 50))


# def cardDis(x, y):
#     randomCard = random.randint(0, len(deck) - 1)
#     gameDisplay.blit(deck[randomCard].image, (x, y))



menu()
pygame.quit()
quit()