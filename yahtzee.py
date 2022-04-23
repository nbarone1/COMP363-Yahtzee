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
ASSET_PATH = f"{os.environ['HOME']}/github_repos/yahtzee/assets" 

# Init pygame
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yahtzee")

# Fonts and Text
# TODO: Clean this up; remove redundancies
title_font = pygame.font.SysFont("firacode", 32)
score_font = pygame.font.SysFont("firacode", 32)
options_font = pygame.font.SysFont("firacode", 16)

title_label = title_font.render("Would You like to roll? Y/N", True, (255, 255, 255))
score_label = score_font.render("Score:", True, (255, 255, 255))
player_options = options_font.render("Options: ", True, (255, 255, 255))

# Load images
dice1 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice1.jpg"), (WIDTH//14, HEIGHT//11))
dice2 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice2.jpg"), (WIDTH//14, HEIGHT//11))
dice3 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice3.jpg"), (WIDTH//14, HEIGHT//11))
dice4 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice4.jpg"), (WIDTH//14, HEIGHT//11))
dice5 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice5.jpg"), (WIDTH//14, HEIGHT//11))
dice6 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice6.jpg"), (WIDTH//14, HEIGHT//11))

# Indexed list to reference all the faces
global dice_list
dice_list = [None, dice1, dice2, dice3, dice4, dice5, dice6]
pygame.display.set_icon(dice6)

# Game Background
background = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/gameboard.jpg"), (WIDTH, HEIGHT))

# Scorecard
scoreboard = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard.png"), (QUARTER_WIDTH, MIDDLE_HEIGHT*1.75))

# Clock to dictate FPS
clock = pygame.time.Clock()

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


def refresh(dice, player_options=None, player_score=None):
    # Repaint the screen
    window.blit(background, (0, 0))
    window.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 250))
    window.blit(score_label, (QUARTER_WIDTH//2 - score_label.get_width()//2, HEIGHT-40))
    #window.blit(scoreboard, (25, 50))
    #window.blit(scoreboard, (3*QUARTER_WIDTH-25, 50))
    
    # Paint the dice faces
    if dice != None:
        for i, die in enumerate(dice):
            window.blit(dice_list[die], [(1.3+(i*0.3))*QUARTER_WIDTH, MIDDLE_HEIGHT])
    # Paint player options
    if player_options != None:
        window.blit(player_options, (QUARTER_WIDTH*2 - player_options.get_width()//2, HEIGHT//2+100))

    # Paint player score
    # if player_score != None

def main():
    running = True
    dice = None
    p1 = player.Player("Player 1")
    p2 = player.Player("Player 2")
    # Initialize board
    refresh(dc.roll())
    freeze = [0,0,0,0,0]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                # Start game
                if event.key == pygame.K_y:
                    dice = dc.roll()
                    options = p1.player_options(dice)
                    # Edit options label to current options
                    player_options = options_font.render(f"Options: {options}", True, (255, 255, 255))
                    refresh(dice, player_options)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Select Dice
                x,y = event.pos
                for i, d in enumerate(dice_list):
                    if d != None:
                        coords = ((1.3+((i-1)*0.3))*QUARTER_WIDTH+(WIDTH//28), MIDDLE_HEIGHT+HEIGHT//22)
                        if d.get_rect(center=coords).collidepoint(x,y):
                            freeze[i-1] = i
                            print(freeze)


            #running = keypress(event, p1)
        pygame.display.flip()
        # Constrain FPS
        clock.tick(FPS)

    pygame.quit()

if __name__=='__main__':
    main()
