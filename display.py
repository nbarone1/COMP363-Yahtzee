import pygame
import random
import os
import yahtzee as yt

# Constants
WIDTH = 1300
HEIGHT = 750
FPS = 60
QUARTER_WIDTH = WIDTH//4
MIDDLE_HEIGHT = HEIGHT//2
ASSET_PATH = f"{os.environ['HOME']}/github_repos/yahtzee/assets" 

# Init game
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yahtzee")

# Fonts and Text
title_font  = pygame.font.SysFont("comicsans", 32)
title_label = title_font.render("Would You like to roll? Y/N", 1, (255, 255, 255))

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
               
def rollDice():
    """ Roll 5 dice """
    return [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]

clock = pygame.time.Clock()
running = True
result1=result2=result3=result4=result5=None

curr_roll = None
while running:

    # handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                curr_roll = yt.roll()

                result1 = dice_list[curr_roll[0]]
                result2 = dice_list[curr_roll[1]]
                result3 = dice_list[curr_roll[2]]
                result4 = dice_list[curr_roll[3]]
                result5 = dice_list[curr_roll[4]]

    # Repaint the screen
    window.blit(background, (0, 0))
    window.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 250))
    window.blit(scoreboard, (25, 50))
    window.blit(scoreboard, (3*QUARTER_WIDTH-25, 50))
    
    # Paint the dice faces
    if curr_roll != None:
        window.blit(result1, (1.3*QUARTER_WIDTH, MIDDLE_HEIGHT))
        window.blit(result2, (1.6*QUARTER_WIDTH, MIDDLE_HEIGHT))
        window.blit(result3, (1.9*QUARTER_WIDTH, MIDDLE_HEIGHT))
        window.blit(result4, (2.2*QUARTER_WIDTH, MIDDLE_HEIGHT))
        window.blit(result5, (2.5*QUARTER_WIDTH, MIDDLE_HEIGHT))
    
    # flush display changes
    pygame.display.flip()
            
    # Constrain FPS
    clock.tick(FPS)

pygame.quit()
