import enum
from gc import freeze
import pygame
import os
import player
import dice as dc

# Constants
WIDTH = 1300
HEIGHT = 750
FPS = 60
QUARTER_WIDTH = WIDTH//4
MIDDLE_HEIGHT = HEIGHT//2
ASSET_PATH = f"{os.getcwd()}\\assets" 

# Init pygame
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yahtzee")

# Fonts and Text
title_font = pygame.font.SysFont("firacode", 32)
score_font = pygame.font.SysFont("firacode", 32)
title_label = title_font.render("Would You like to roll? Y/N", True, (255, 255, 255))
score_label = score_font.render("Score:", True, (255, 255, 255))

# Load images
dice1 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}\\alt-die\\dice1.svg"), (WIDTH//14, HEIGHT//12))
dice2 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}\\alt-die\\dice2.svg"), (WIDTH//14, HEIGHT//12))
dice3 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}\\alt-die\\dice3.svg"), (WIDTH//14, HEIGHT//12))
dice4 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}\\alt-die\\dice4.svg"), (WIDTH//14, HEIGHT//12))
dice5 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}\\alt-die\\dice5.svg"), (WIDTH//14, HEIGHT//12))
dice6 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}\\alt-die\\dice6.svg"), (WIDTH//14, HEIGHT//12))

# Indexed list to reference all the faces
dice_list = [None, dice1, dice2, dice3, dice4, dice5, dice6]
pygame.display.set_icon(dice6)

# Game Background
background = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}\\gameboard.jpg"), (WIDTH, HEIGHT))

# Scorecard
scoreboard = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}\\scorecard.png"), (QUARTER_WIDTH, MIDDLE_HEIGHT*1.75))

# Clock to dictate FPS
clock = pygame.time.Clock()

# Handle user input
# Returns running status
def event_handler(player, dice=None):
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            # Start game
            if event.key == pygame.K_y:
                dice = dc.roll()
                #gameloop(player, dc.roll())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            # Click on dice
            for die in dice_list:
                if die.get_rect().collidepoint(x,y):
                    window.blit()
                    print("yes")
        return True


def player_create():
    # create list of players 

    player_list = []

    window.blit(background, (0, 0)

    # input rect
    input_rect = pygame.Rect(200, 200, 140, 32)

    # define font
    base_font = pygame.font.Font(None, 32)
    # color for input background and letters
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    prompt_label = base_font.render("Enter Number of Players: ",True, (255, 255, 255))

    numberplayers = 0
    while True:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:

            # If return, create player

            if event.type == pygame.K_RETURN:
                return

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                numberplayers = numberplayers[:-1]

            # Unicode standard is used for string
            # formation
            else:
                if event.unicode.isnumeric():
                    numberplayers += event.unicode

            screen.fill((255, 255, 255))
  
            if active:
                color = color_active
            else:
                color = color_passive
        
        # bring it to life
        pygame.draw.rect(window, color, input_rect)

        text_surface = base_font.render(numberplayers, True, (255,255,255))

        # set position
        window.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        # limit width so text cannot go outside of view

        input_rect.w = max(100, text_surface.get_width()+10)
        #update screen
        pygame.display.flip()

        #update how long should pass
        clock.tick(60)

    for x in range(numberplayers):
        name = ""
        for even in pygame.event.get():
            user_text = ""
            while True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
        
                if event.type == pygame.KEYDOWN:

                    # If return, create player

                    if event.type == pygame.K_RETURN:
                        name = user_text
                        return
        
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
        
                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
        
                    # Unicode standard is used for string
                    # formation
                    else:
                        user_text += event.unicode

                    #
                    screen.fill((255, 255, 255))
  
                    if active:
                        color = color_active
                    else:
                        color = color_passive
                # bring it to life
                pygame.draw.rect(window, color, input_rect)

                text_surface = base_font.render(user_text, True, (255,255,255))

                # set position
                window.blit(text_surface, (input_rect.x+5, input_rect.y+5))

                # limit width so text cannot go outside of view

                input_rect.w = max(100, text_surface.get_width()+10)
                #update screen
                pygame.display.flip()

                #update how long should pass
                clock.tick(60)

        pl = player.Player(name)
        player_list.append(pl)

    return player_list

# Mark scorcard with current player selection. Update scorecard
def gameloop(player, dice=None, rerolls=2):
    # Calculate options based on roll
    
    # TODO: Show dice

    options = player.player_options(dice)

def quit(event):
    if event.type == pygame.QUIT:
        return False


# Handle user input
# Returns running status
def keypress(event, player, dice=None):
    # Quit
    if quit(event): return False

    elif event.type == pygame.KEYDOWN:
        # Start game
        if event.key == pygame.K_y:
            refresh(dc.roll())
            gameloop(player, dc.roll())
    return True

def mousepress(event):
    # Quit
    if quit(event): return False

    elif event.type == pygame.MOUSEBUTTONDOWN:
        x,y = event.pos
        for i, d in enumerate(dice_list):
            if d != None:
                coords = ((1.3+((i-1)*0.3))*QUARTER_WIDTH+(WIDTH//28), MIDDLE_HEIGHT+HEIGHT//22)
                if d.get_rect(center=coords).collidepoint(x,y):
                    print(i)


# Mark scorcard with current player selection. Update scorecard
def gameloop(player, dice, rerolls=2):
    # Calculate options based on roll
    
    # TODO: Show dice
    options = player.player_options(dice)
    # Edit options label to current options
    player_options = options_font.render(f"Options: {options}", True, (255, 255, 255))
    refresh(dice, player_options)

    mousepress(event)
    '''
    if rerolls == 0:
        return
    elif rerolls > 0:
        freeze = list(map(int, pick.replace(',', ' ').split()))
        print(freeze)
        dice = dice.roll(dice, freeze)
        rerolls-=1
        gameloop(dice, player, rerolls)     
    '''

    '''
    # TODO: Display list of options

    if rerolls > 0:
        # TODO: Display text below
        print('Enter a valid scorecard option, or choose which dice to freeze')
    else:
        # TODO: Display text below
        print('Enter a valid scorecard option')

    # TODO: Integrate a pick option in pygame 
    pick = input()

    # Base case
    # Mark scorcard with current player selection. Update scorecard
    if pick in options.keys():
        if player.scorecard[pick] == 0:
            print(f'"{pick}" selected')
            # TODO: Highlight die that have been selected
            player.scorecard[pick] = options[pick] 
            player.player_score += options[pick]
    elif pick == "":
        print("Pass")
    elif rerolls > 0:
        freeze = list(map(int, pick.replace(',', ' ').split()))
        print(freeze)
        dice = dice.roll(dice, freeze)
        rerolls-=1
        gameloop(dice, player, rerolls)     
    else:
        print("Not a valid option or no rerolls left, select a valid scorecard option")
        gameloop(dice, player, rerolls)     
    '''


def refresh(dice, freeze, player_options=None, player_score=None):
    # Repaint the screen
    window.blit(background, (0, 0))
    window.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 250))
    window.blit(score_label, (QUARTER_WIDTH//2 - score_label.get_width()//2, HEIGHT-40))
    #window.blit(scoreboard, (25, 50))
    #window.blit(scoreboard, (3*QUARTER_WIDTH-25, 50))
    
    # Paint the dice faces
    if dice != None and freeze != None:
        for i, (die, f) in enumerate(zip(dice, freeze)):
            window.blit(dice_list[die], [(1.3+(i*0.3))*QUARTER_WIDTH, MIDDLE_HEIGHT])
            if f != 0:
                pixel_rect = dice_list[die].get_bounding_rect()
                trimmed_surface = pygame.Surface(pixel_rect.size)
                trimmed_surface.blit(dice_list[die], (0,0), pixel_rect)
    # Paint player options
    if player_options != None:
        window.blit(player_options, (QUARTER_WIDTH*2 - player_options.get_width()//2, HEIGHT//2+100))

    # Paint player score
    # if player_score != None

def main():
    running = True
    dice = None
    player_create()
    p1 = player.Player("Player 1")
    p2 = player.Player("Player 2")
    # Initialize board
    freeze = [0,0,0,0,0]
    refresh(dc.roll(dice, freeze), freeze)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                # Start game
                if event.key == pygame.K_r:
                    dice = dc.roll(dice, freeze)
                    options = p1.player_options(dice)
                    # Edit options label to current options
                    player_options = options_font.render(f"Options: {options}", True, (255, 255, 255))
                    refresh(dice, freeze, player_options)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Select Dice
                x,y = event.pos
                for i, d in enumerate(dice_list):
                    if d != None:
                        coords = ((1.3+((i-1)*0.3))*QUARTER_WIDTH+(WIDTH//28), MIDDLE_HEIGHT+HEIGHT//22)
                        if d.get_rect(center=coords).collidepoint(x,y):
                            if freeze[i-1] != 0:
                                freeze[i-1] = 0
                            else:
                                freeze[i-1] = i
                            print(freeze)


            #running = keypress(event, p1)
        pygame.display.flip()
        # Constrain FPS
        clock.tick(FPS)

    pygame.quit()

if __name__=='__main__':
    main()
