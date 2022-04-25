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
global dice_list
dice_list = [None, dice1, dice2, dice3, dice4, dice5, dice6]
pygame.display.set_icon(dice6)

# Game Background
background = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/gameboard.jpg"), (WIDTH, HEIGHT))

# Scorecard
scoreboard = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard.png"), (QUARTER_WIDTH, MIDDLE_HEIGHT*1.75))

# Clock to dictate FPS
clock = pygame.time.Clock()

# This function got cut off when I was editing diffs for some reason
''' 
def player_creation():
    # Start event handler
    for event in pygame.event.get():
        if event.type == pygame.
'''

def refresh(dice):

    # Repaint the screen
    window.blit(background, (0, 0))
    window.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 250))
    window.blit(score_label, (QUARTER_WIDTH//2 - score_label.get_width()//2, HEIGHT-40))
    #window.blit(scoreboard, (25, 50))
    #window.blit(scoreboard, (3*QUARTER_WIDTH-25, 50))
    
    # Paint the dice faces
    if dice != None and freeze != None:
        for i, (die, f) in enumerate(zip(dice, freeze)):
            width = (1.1+(i*0.4))*QUARTER_WIDTH
            height = MIDDLE_HEIGHT
            if f != 0:
                pygame.draw.rect(window, (255,0,0), pygame.Rect(width-5, height-5, 105, 80))
            window.blit(dice_list[die], [width, height])
            
    # Paint player options
    if player_options != None:
        window.blit(player_options, (QUARTER_WIDTH*2 - player_options.get_width()//2, HEIGHT//2+100))


def dice_roll(player, dice, freeze):
    options = player.player_options(dice)
    # Edit options label to current options
    player_options = options_font.render(f"Options: {options}", True, (255, 255, 255))
    refresh(dice, freeze, player_options)

    
def dice_freeze(x, y, dice, freeze):
    for i, d in enumerate(dice_list):
        if d != None:
            coords = ((1.1+((i-1)*0.4))*QUARTER_WIDTH+(WIDTH//28), MIDDLE_HEIGHT+HEIGHT//22)
            if d.get_rect(center=coords).collidepoint(x,y):
                if freeze[i-1] != 0:
                    freeze[i-1] = 0
                else:
                    freeze[i-1] = i
                refresh(dice, freeze)
                print(freeze)


def main():
    running = True
    dice = dc.roll(None, None)
    p1 = player.Player("Player 1")
    p2 = player.Player("Player 2")
    # Initialize board
    freeze = [0,0,0,0,0]
    refresh(dice, freeze)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                # Start game
                if event.key == pygame.K_r:
                    dice = dc.roll(dice, freeze)
                    dice_roll(p1, dice, freeze)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Select Dice
                x,y = event.pos
                dice_freeze(x,y, dice, freeze)

        pygame.display.flip()
        # Constrain FPS
        clock.tick(FPS)

    pygame.quit()


if __name__=='__main__':
    main()
