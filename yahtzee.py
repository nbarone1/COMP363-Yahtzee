import pygame
import random
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
title_font = pygame.font.SysFont("firacode", 32)
score_font = pygame.font.SysFont("firacode", 32)
title_label = title_font.render("Would You like to roll? Y/N", True, (255, 255, 255))
score_label = score_font.render("Score:", True, (255, 255, 255))

# Load images
dice1 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice1.svg"), (WIDTH//14, HEIGHT//12))
dice2 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice2.svg"), (WIDTH//14, HEIGHT//12))
dice3 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice3.svg"), (WIDTH//14, HEIGHT//12))
dice4 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice4.svg"), (WIDTH//14, HEIGHT//12))
dice5 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice5.svg"), (WIDTH//14, HEIGHT//12))
dice6 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice6.svg"), (WIDTH//14, HEIGHT//12))

# Indexed list to reference all the faces
dice_list = [None, dice1, dice2, dice3, dice4, dice5, dice6]
pygame.display.set_icon(dice6)

# Game Background
background = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/gameboard.jpg"), (WIDTH, HEIGHT))

# Scorecard
scoreboard = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard.png"), (QUARTER_WIDTH, MIDDLE_HEIGHT*1.75))

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
                    print("yes")
        return True


# Mark scorcard with current player selection. Update scorecard
def gameloop(player, dice=None, rerolls=2):
    # Calculate options based on roll
    
    # TODO: Show dice

    options = player.player_options(dice)

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


def refresh(dice):
    # Repaint the screen
    window.blit(background, (0, 0))
    window.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 250))
    window.blit(score_label, (QUARTER_WIDTH//2 - score_label.get_width()//2, HEIGHT-40))
    window.blit(scoreboard, (25, 50))
    window.blit(scoreboard, (3*QUARTER_WIDTH-25, 50))
    
    # Paint the dice faces
    if dice != None:
        for i, die in enumerate(dice):
            window.blit(dice_list[die], ((1.3+(i*0.3))*QUARTER_WIDTH, MIDDLE_HEIGHT))

def main():
    running = True
    dice = None
    p1 = player.Player("Player 1")
    p2 = player.Player("Player 2")

    while running:

        event_handler(p1)
        # Repaint the screen
        refresh(dice)
        # flush display changes
        pygame.display.flip()
        # Constrain FPS
        clock.tick(FPS)

    pygame.quit()

if __name__=='__main__':
    main()
