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
ASSET_PATH = '/home/nick/github_repos/yahtzee/assets'

# Init pygame
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yahtzee")

# Fonts and Text
title_font = pygame.font.SysFont("firacode", 32)
score_font = pygame.font.SysFont("firacode", 32)
options_font = pygame.font.SysFont("firacode", 16)

title_label = title_font.render("Press 'r' to roll dice", True, (255, 255, 255))
score_label = score_font.render("Score:", True, (255, 255, 255))

# Load images
dice1 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice1.jpg"), (WIDTH//14, HEIGHT//12))
dice2 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice2.jpg"), (WIDTH//14, HEIGHT//12))
dice3 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice3.jpg"), (WIDTH//14, HEIGHT//12))
dice4 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice4.jpg"), (WIDTH//14, HEIGHT//12))
dice5 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice5.jpg"), (WIDTH//14, HEIGHT//12))
dice6 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice6.jpg"), (WIDTH//14, HEIGHT//12))

# Indexed list to reference all the faces
global dice_list
dice_list = [None, dice1, dice2, dice3, dice4, dice5, dice6]
pygame.display.set_icon(dice6)

# Game Background
background = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/gameboard.jpg"), (WIDTH, HEIGHT))
# Scorecard
scoreboard = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard.png"), (QUARTER_WIDTH, MIDDLE_HEIGHT*1.75))
title_slide = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/title_screen.jpg"), (WIDTH, HEIGHT))
game_over = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/game_over.jpg"), (WIDTH, HEIGHT))

# Clock to dictate FPS
clock = pygame.time.Clock()

# input rect
input_rect = pygame.Rect(200, 200, 140, 32)

# define font
base_font = pygame.font.Font(None, 32)

def player_numbers():
    # set number of players 

    window.blit(background, (0, 0))

    # color for input background and letters
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    prompt_label = base_font.render("Enter Number of Players: ",True, (255, 255, 255))

    numberplayers = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:

                # If return, create player

                if event.key == pygame.K_RETURN:
                    return numberplayers

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    numberplayers = numberplayers[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    if event.unicode.isnumeric():
                        numberplayers += event.unicode
    
                if active:
                    color = color_active
                else:
                    color = color_passive
            
            # bring it to life
            pygame.draw.rect(window, color, input_rect)

            text_surface = base_font.render(numberplayers, True, (255,255,255))

            # set position
            window.blit(prompt_label, (WIDTH//2 - prompt_label.get_width()//2, 250))
            window.blit(text_surface, (input_rect.x+5, input_rect.y+5))

            # limit width so text cannot go outside of view

            input_rect.w = max(100, text_surface.get_width()+10)
            #update screen
            pygame.display.flip()

            #update how long should pass
            clock.tick(60)

def create_player(x):
    # create individual players

    # color for input background and letters
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    window.blit(background, (0, 0))

    prompt_label = base_font.render("Enter Player #{} Name: ".format(x),True, (255, 255, 255))
    name = ""
    user_text = ""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
    
            if event.type == pygame.KEYDOWN:

                # If return, create player

                if event.key == pygame.K_RETURN:
                    name = user_text
                    return player.Player(name)
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
    
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode

                if active:
                    color = color_active
                else:
                    color = color_passive
            # bring it to life
            pygame.draw.rect(window, color, input_rect)

            text_surface = base_font.render(user_text, True, (255,255,255))

            # set position
            window.blit(prompt_label, (WIDTH//2 - prompt_label.get_width()//2, 250))
            window.blit(text_surface, (input_rect.x+5, input_rect.y+5))

            # limit width so text cannot go outside of view

            input_rect.w = max(100, text_surface.get_width()+10)
            #update screen
            pygame.display.flip()

            #update how long should pass
            clock.tick(60)

            
def player_create():
    # create player list
    player_list = []
    numplayer = int(player_numbers())
    for x in range(1,numplayer+1):
        player_list.append(create_player(x))
    return player_list


def refresh(dice, freeze, player_options=None, player_score=None):
    # Repaint the screen
    window.blit(background, (0, 0))
    window.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 250))
    window.blit(score_label, (QUARTER_WIDTH//2 - score_label.get_width()//2, HEIGHT-40))
    window.blit(scoreboard, (25, 50))
    #window.blit(scoreboard, (3*QUARTER_WIDTH-25, 50))
    
    # Paint the dice faces
    if dice != None and freeze != None:
        for i, (die, f) in enumerate(zip(dice, freeze)):
            width = (1.4+(i*0.4))*QUARTER_WIDTH
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
            coords = ((1.4+((i-1)*0.4))*QUARTER_WIDTH+(WIDTH//28), MIDDLE_HEIGHT+HEIGHT//22)
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
    #player_list = player_create()
    #print(player_list)
    p1 = player.Player("Player 1")
    p2 = player.Player("Player 2")
    # Initialize board
    freeze = [0,0,0,0,0]
    window.blit(title_slide, (0, 0))
    #refresh(dice, freeze)

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
