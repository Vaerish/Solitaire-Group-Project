import pygame
import time
import random

pygame.init()

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)  # color definitions
gray = (167, 171, 167)
red = (153, 18, 18)
green = (47, 110, 41)
cyan = (0,238,238)
OLIVE = (128,128,0)
turquoise = (46, 204, 105)

bright_red = (46, 7, 7)
bright_green = (16, 34, 14)

display_width = 1280
display_height = 720
crashed = False

card_width = 100 
card_length = 150



"""
    Changing from Leo
"""

card_dict = {} #This variable will hold all the images of the cards
################################# Leo'code ********************************
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


snowboots = pygame.image.load("Snowboots the beautiful.jpg")
snowboots = pygame.transform.scale(snowboots, (1280, 1100))
whiteBackground = pygame.image.load("White-Background.jpg")
whiteBackground = pygame.transform.scale(whiteBackground, (1280, 720))
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

# generates a complete list of Cards
def generateDeck():
    deck = []
    for suit in SUITS:
        for face in FACES:
            card = Card(face, suit)
            card_dict[face+suit] = pygame.image.load("Cards/PNG/{}{}.png".format(face, suit))
            card_dict[face+suit] = pygame.transform.scale(card_dict[(str)(face+suit)], (card_width, card_length))
            deck.append(card)
    return deck



deck = generateDeck()

'''
    Changing from Leo
'''
class Moved_card(object):
    moved = False
    moved_card = []
    card_d = ()
    cards = None
    """
        this is called when user realase mouse button
    """
    def click_up(self,deck_list):
        if(len(self.moved_card)) > 0 :
            for item in deck_list:  
                if item.check_pos() and item.check_card(self.moved_card,pygame.mouse.get_pos()):
                    item.add_card(self.moved_card)
                    self.moved = False
                    self.moved_card = []
                    # if isinstance(self.cards, Deck_Tableu):
                    #     self.cards.show_card()
                    self.cards = None
                    break
            else: #els statement must be same line with for, 
                if self.cards is not None:
                    self.cards.add_card(self.moved_card)
                self.moved = False
                self.moved_card = []
                self.cards = None    

    def draw(self,screen,card_dict):
        """This draw the moved cards onto the screen"""
        if self.moved:
            pos = pygame.mouse.get_pos()
            x = pos[0] - self.card_d[0]
            y = pos[1] - self.card_d[1]
            for item in self.moved_card:
                screen.blit(card_dict[(str)(item)],[x,y])
                y += 32



    


class Deck_Tableu:
    def __init__(self,x,y):
        #call parent's constructor:
        self.cards = []
        self.rect = pygame.Rect(x,y,card_length,card_width)
        self.y = y
    """

    """
    def check_pos(self):
        """ this check if the cursor is on the card"""
        pos = pygame.mouse.get_pos()
        if pos[0] >= self.rect.left and pos[0] <= self.rect.right:
            if pos[1] >= self.rect.top and pos[1] <= self.rect.bottom:
                return True
            else:
                return False
        else:
            return False

    def draw_card(self,screen,card_dict):
        """This will draw all the cards on the screen"""
        pygame.draw.rect(screen,black,[self.rect.left,self.rect.top,card_width,card_length],2)
        i = self.y
        # if len(self.hidden) > 0:
        #     for item in self.hidden:
        #         pygame.draw.rect(screen,cyan,[self.rect.left,i,card_width,card_length])
        #         pygame.draw.rect(screen,black,[self.rect.left,i,card_width,card_length],2)
        #         i += 32
        if len(self.cards) > 0:          
            for item in self.cards:             
                gameDisplay.blit(card_dict[(str)(item)],(self.rect.left,i))
                i += 32
                
    def add_card(self,card):
        if len(self.cards) > 0 :
            for i in range(len(card)):
                self.rect.top += 32
        else:
            for i in range(len(card)):
                if i > 0:
                    self.rect.top += 32
        self.cards.extend(card)

    def click_down(self,card):
        """This is used when the user press the mouse button"""
        if len(self.cards) > 0:
            top = self.rect.top
            lst = []
            for i in range(len(self.cards)):
                if self.check_pos():
                    pos = pygame.mouse.get_pos()
                    lst.insert(0,self.cards.pop())
                    card.card_d = (pos[0] - self.rect.left,pos[1] -
                                   self.rect.top)
                    card.moved = True
                    card.cards = self
                    card.moved_card.extend(lst)
                    if len(self.cards) > 0:
                        self.rect.top -= 32
                    break
                else:
                    lst.insert(0,self.cards.pop())
                    self.rect.top -= 32
            else:
                self.rect.top = top
                self.cards.extend(lst)

    # def show_card(self):
    #     if len(self.cards) == 0:
    #         self.cards.append()

    """
        I have to use this way to run the game logic, please replaces with your recursion logic
    """
    def check_card(self,moved_card, mouse_position):
        card = moved_card[0]   
        result = False
        """
            first if statement uses for free space at the top
        """
        if len(self.cards)==0 and mouse_position[0] <= 500 and mouse_position[0]>=700 :
            result == True
        """
            this if statement is game logic, it seems works to me, but I am 
            no idea how to play this game
        """
        if len(self.cards) == 0:
            if "A" == card.face :
                result = True
        else:
            if "H" == card.suit or "D" == card.suit:
                if "S" == self.cards[-1].suit or "C" == self.cards[-1].suit:
                    next_card = "X"
                    if "A" == self.cards[-1].face:
                        next_card = "K"
                    elif "K" == self.cards[-1].face:
                        next_card = "Q"
                    elif "Q" == self.cards[-1].face:
                        next_card = "J"
                    elif "J" == self.cards[-1].face:
                        next_card ="10"
                    elif "10" in self.cards[-1].face:
                        next_card = "9"
                    elif "9" in self.cards[-1].face:
                        next_card = "8"
                    elif "8" in self.cards[-1].face:
                        next_card = "7"
                    elif "7" in self.cards[-1].face:
                        next_card = "6"

                    if next_card == card.face:
                        result = True
            elif "H" == self.cards[-1].suit or "D" == self.cards[-1].suit:
                next_card = "X"
                if "A" in self.cards[-1].face:
                    next_card = "K"
                elif "K" in self.cards[-1].face:
                    next_card = "Q"
                elif "Q" in self.cards[-1].face:
                    next_card = "J"
                elif "J" in self.cards[-1].face:
                    next_card = "10"
                elif "10" in self.cards[-1].face:
                    next_card = "9"
                elif "9" in self.cards[-1].face:
                    next_card = "8"
                elif "8" in self.cards[-1].face:
                    next_card = "7"
                elif "7" in self.cards[-1].face:
                    next_card = "6"
                if next_card == card.face:
                    result = True

        return result


class Deck_Waste:
    def __init__(self,x,y):
        #call parent's constructor:
        self.cards = []
        self.rect = pygame.Rect(x,y,card_width,card_length)

    def check_pos(self):
        """This check if the cursor is on the card"""
        pos = pygame.mouse.get_pos()
        print(pos)
        if pos[0] >= self.rect.left and pos[0] <= self.rect.right:
            if pos[1] >= self.rect.top and pos[1] <= self.rect.bottom:
                return True
            else:
                return False
        else:
            return False

    def check_card(self,moved_card, mouse_position):
        if(len(moved_card) == 1):
            card = moved_card[0]
            if(len(self.cards)==0):
                return True

    def click_down(self,card):
        """This is used when the user press the mouse button"""
        if self.check_pos() and len(self.cards) > 0:
            pos = pygame.mouse.get_pos()
            card.moved_card.append(self.cards.pop())
            card.card_d = (pos[0] - self.rect.left,pos[1] - self.rect.top)
            card.moved = True
            card.cards = self

    def add_card(self,card):
        self.cards.extend(card)

    def draw_card(self,screen,card_dict):
        """This will draw all the cards on the screen"""
        pygame.draw.rect(screen,black,[self.rect.left,self.rect.top,card_width,card_length],2)
        if len(self.cards) > 0:
            screen.blit(card_dict[(str)(self.cards[-1])],[self.rect.left,self.rect.top])







# faceDown = pygame.image.load('Cards/PNG/gosnel.jpg')
# faceDown = pygame.transform.scale(faceDown,(card_width,card_length))


# generates a complete list of Cards
# def generateDeck():
#     deck = []
#     for suit in SUITS:
#         for face in FACES:
#             card = Card(face, suit)
#             deck.append(card)
#     return deck



# deck = generateDeck()

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
    textSurf, textRect = text_objects(msg, smallText, black)
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


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText, black)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    return


# function will randomly generates the cards in desk array and place on the UI
# NOTE: should rezise or rescale the cards to make sure they can fix for all seven piles
def shuffle():
    ############################### Old code #################################################### 
    # piles =[]
    # x = (display_width * 0.25)
    # y = (display_height * .5)
    # for index in range(100, 1100, 200):
    #     # cardDis(index, y)
    #     piles.append(Pile(random.randint(0, len(deck) - 1),index,y))
    # for pile in piles:
    #     gameDisplay.blit(deck[pile.card].image, (pile.x, pile.y))
    #     print(deck[pile.card])
    # pygame.display.update()

    ############################# New code #####################################################
    """This shuffle the cards"""
    r = []
    deck = generateDeck()
    length = len(deck)
    for i in range(length):
        if len(deck) > 1:
            c = random.choice(deck)
            r.append(c)
            deck.remove(c)
        else:
            c = deck.pop()
            r.append(c)

    return r


# if you want to actually run game call game() at bottom as opposed to menu()
# I am working on a button to link between them though
def game(isWin = None):
    mouse = pygame.mouse.get_pos()
    layout(gameDisplay)
    pygame.mixer.music.load("Elevator-music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    global crashed
    isReset = False
    isGiveUp = False
    
    x = (display_width * 0.25)
    y = (display_height * .5)

    ######################### Leo's code ##############################################################
    card_list = shuffle() if isWin is None else winning_Deck()
    deck_list =[]
    counter =30
    for i in range(9):
        deck_list.append(Deck_Tableu(counter,250))
        counter +=140
   #The code below will distribute all the cards on the tablue piles.  
    for i in range(len(deck_list)):
        deck_list[i].add_card(card_list[:4])
        del card_list[:4]
    deck_list.append(Deck_Waste(500,0))
    # deck_list.append(Deck_Waste(300,0))
    # deck_list.append(Deck_Waste(100,0))


    m_card = Moved_card()
    game_over = False
    font = pygame.font.Font(None,25)
    text = font.render("Congratulations, You Won!",True,black)   
 ##########################################################################################   
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.mixer.music.stop()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0]>=700 and mouse[0]<=800:
                    if mouse[1]>=0 and mouse[1]<=100:
                        isReset = True
                if mouse[0]>=900 and mouse[0]<=1000:
                    if mouse[1]>=0 and mouse[1]<=100:
                        isGiveUp = True              
                for item in deck_list:
                    item.click_down(m_card)
                
                
            if event.type == pygame.MOUSEBUTTONUP:
                m_card.click_up(deck_list)

                
                    
        gameDisplay.fill(turquoise)
        gameDisplay.blit(whiteBackground, (0, 0))
        # pygame.draw.ellipse(gameDisplay,OLIVE,[122,40,60,60],5)
        # pygame.draw.ellipse(gameDisplay,OLIVE,[322,40,60,60],5)
        pygame.draw.ellipse(gameDisplay,OLIVE,[522,40,60,60],5)
        fullStack = 0
        emptyPileCounter = 0
        for item in deck_list:
            if(len(item.cards) == 0):
                emptyPileCounter = emptyPileCounter + 1
            elif(len(item.cards) == 9 and item.cards[0].face == "A"):
                fullStack = fullStack +1          
            item.draw_card(gameDisplay,card_dict)
        m_card.draw(gameDisplay,card_dict)
        if(emptyPileCounter == 6 and fullStack ==4):
                pygame.draw.rect(gameDisplay,cyan,[230,200,250,25])
                gameDisplay.blit(text,[250,200])
        ###########################################################################
        # this function uses to create a button to shuffering the cards
        # It is used for testing purpose but could be use in the game
        # when the player need refresh the cards from Draw Pile or restart the game
        # #########################################################################
        if isReset is True:
            button("Refresh", 700, 0, 100, 100, white, gray, reset(m_card))
            isReset = False
        elif isGiveUp is True:
            button("Winning", 900, 0, 100, 100, white, gray,reset(m_card,isGiveUp))
            isGiveUp = False
        button("Refresh", 700, 0, 100, 100, white, gray)
        button("Winning", 900, 0, 100, 100, white, gray)
        button("Leave Game", 1100, 0, 150, 100, cyan, red, quitInGame)
   
        pygame.display.flip()
        clock.tick(20)

def reset(moved_card,isWin=None):
    moved_card.moved_card == []
    game(isWin)

def winning_Deck():
    return [Card("A", "D"), Card("K", "S"), Card("Q", "D"), Card("J", "S"), 
            Card("10", "D"), Card("9", "S"),Card("8", "D"),Card("7", "S"),
            Card("6", "D"),Card("A", "H"),Card("K", "C"),Card("Q", "H"),
            Card("J", "C"),Card("10", "H"),Card("9", "C"),Card("8", "H"),Card("7", "S"),Card("6", "H"),
            Card("A", "S"), Card("K", "D"), Card("Q", "S"), Card("J", "D"), 
            Card("10", "S"), Card("9", "D"),Card("8", "S"),Card("7", "D"),
            Card("6", "S"),Card("A", "C"),Card("K", "H"),Card("Q", "C"),
            Card("J", "H"),Card("10", "C"),Card("9", "H"),Card("8", "C"),Card("7", "H"),Card("6", "C")]


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
        ruleText = pygame.font.Font("freesansbold.ttf", 26)
        # create a text suface object,
        # on which text is drawn on it.
        TextSurf, TextRect = text_objects('Number cards are stacked by alternating color and decreasing value,',ruleText, black)
        TextRect.center = ((display_width / 2), (display_height / 3))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('and can be moved together as a stack of any size.', ruleText, black)
        TextRect.center = ((display_width / 2), (display_height / 3) + 40)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Face cards are stacked by suit and in any order, and can also be moved as a stack.', ruleText, black)
        TextRect.center = ((display_width / 2), (display_height / 3) + 80)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('However, a completed stack of face cards placed directly on the board will become immovable', ruleText, black)
        TextRect.center = ((display_width / 2), (display_height / 3) + 120)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('To win, sort the dealt cards into four completed  stacks of number cards and ', ruleText, black)
        TextRect.center = ((display_width / 2), (display_height / 3) + 160)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('four complete stacks of face cards. The free cell in the corner can store a single card of any type.',ruleText, black)
        TextRect.center = ((display_width / 2), (display_height / 3) + 200)
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
        gameDisplay.blit(snowboots, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Solitaire!", largeText, white)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        msg = "Go"
        button(msg, 150, 450, 200, 50, green, bright_green, game)
        button("Quit", 900, 450, 200, 50, red, bright_red, quitGame)
        button("Rules", 500, 450, 200, 50, white, white, rules)
        mouse = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(5)





def layout(screen):
    x = 150
    y = 210
    screen.fill(turquoise)
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
