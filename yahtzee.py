import enum
from gc import freeze
from numpy import rollaxis
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

# Load dice 
dice1 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice1.jpg"), (WIDTH//14, HEIGHT//12))
dice2 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice2.jpg"), (WIDTH//14, HEIGHT//12))
dice3 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice3.jpg"), (WIDTH//14, HEIGHT//12))
dice4 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice4.jpg"), (WIDTH//14, HEIGHT//12))
dice5 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice5.jpg"), (WIDTH//14, HEIGHT//12))
dice6 = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/dice6.jpg"), (WIDTH//14, HEIGHT//12))
# Load scoreboard assets

aces_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/aces_label.jpg"), (QUARTER_WIDTH*0.9, HEIGHT//13))
twos_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/twos_label.jpg"),(QUARTER_WIDTH*0.9, HEIGHT//13)) 
threes_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/threes_label.jpg"),(QUARTER_WIDTH*0.9, HEIGHT//13)) 
fours_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/fours_label.jpg"),(QUARTER_WIDTH*0.9, HEIGHT//13)) 
fives_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/fives_label.jpg"),(QUARTER_WIDTH*0.9, HEIGHT//13)) 
sixes_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/sixes_label.jpg"),(QUARTER_WIDTH*0.9, HEIGHT//13)) 
upper_selection_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/upper_selection.jpg"),(QUARTER_WIDTH*0.9, HEIGHT//13)) 
value_box_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/value_box.jpg"),(QUARTER_WIDTH*0.9, HEIGHT//13)) 

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

# start/finish slides
title_slide = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/title_screen.jpg"), (WIDTH, HEIGHT))
game_over = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/game_over.jpg"), (WIDTH, HEIGHT))

# Clock to dictate FPS
clock = pygame.time.Clock()

# input rect
input_rect = pygame.Rect(600, 400, 140, 32)

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


def start():
    window.blit(title_slide,(0,0))

def end(player_list):
    winner = ""
    max = 0
    for i in range(0,len(player_list)):
        if player_list[i].player_score > max:
            max = player_list[i].player_score
            winner = player_list[i].name
        if player_list[i].player_score == max:
            winner = winner," and ",player_list[i].name," tied"
    
    winnings = base_font.render(f"{winner} wins with a score of {max}", True, (255,255,255))
    quit_message = options_font.render("Press any key to exit",True,(255,255,255))

    window.blit(game_over,(0,0))
    window.blit(winnings,((WIDTH//2 - winnings.get_width()//2),HEIGHT//2))
    window.blit(quit_message,((WIDTH//2 - quit_message.get_width()//2),(HEIGHT//2)-winnings.get_height()//2-quit_message.get_height()))

    for event in pygame.event.get():
        if event.type is pygame.KEYDOWN:
            pygame.quit()


def refresh(dice, freeze, playername=None, player_options=None, player_score=None):
    # Repaint the screen
    window.blit(background, (0, 0))
    window.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 250))
    window.blit(score_label, (QUARTER_WIDTH//2 - score_label.get_width()//2, HEIGHT-40))

    # Repaint scorecard
    window.blit(upper_selection_sc, (25, 5))
    window.blit(aces_sc, (25, 60))
    window.blit(twos_sc, (25, 110))
    window.blit(threes_sc, (25, 160))
    window.blit(fours_sc, (25, 210))
    window.blit(fives_sc, (25, 260))
    window.blit(sixes_sc, (25, 310))
    
    window.blit(value_box_sc, (25+aces_sc.get_width(), 60))
    window.blit(value_box_sc, (25+aces_sc.get_width(), 110))
    window.blit(value_box_sc, (25+aces_sc.get_width(), 160))
    window.blit(value_box_sc, (25+aces_sc.get_width(), 210))
    window.blit(value_box_sc, (25+aces_sc.get_width(), 260))
    window.blit(value_box_sc, (25+aces_sc.get_width(), 310))

    #window.blit(scoreboard, (25, 50))
    #if playername != None:
    #    window.blit(playername,(620,50))

    #window.blit(scoreboard, (3*QUARTER_WIDTH-25, 50))
    
    # Paint the dice faces
    if dice != None and freeze != None:
        for i, (die, f) in enumerate(zip(dice, freeze)):
            width = (1.7+(i*0.4))*QUARTER_WIDTH
            height = MIDDLE_HEIGHT
            if f != 0:
                pygame.draw.rect(window, (255,0,0), pygame.Rect(width-5, height-5, 105, 80))
            window.blit(dice_list[die], [width, height])
            
    # Paint player options
    if player_options != None:
        window.blit(player_options, (QUARTER_WIDTH*2 - player_options.get_width()//2, HEIGHT//2+100))


def dice_roll(player, dice, freeze,rolls):
    options = player.player_options(dice)
    # Print Player's Name on Top
    player_name = base_font.render(f"{player.name}'s Turn with {rolls} rolls remaining", True,(255,255,255))
    # Edit options label to current options
    player_options = options_font.render(f"Options: {options}", True, (255, 255, 255))
    refresh(dice, freeze, player_name,player_options)

    
def dice_freeze(x, y, dice, freeze,play):
    for i, d in enumerate(dice_list):
        if d != None:
            coords = ((1.4+((i-1)*0.4))*QUARTER_WIDTH+(WIDTH//28), MIDDLE_HEIGHT+HEIGHT//22)
            if d.get_rect(center=coords).collidepoint(x,y):
                if freeze[i-1] != 0:
                    freeze[i-1] = 0
                else:
                    freeze[i-1] = i
                refresh(dice, freeze,play)
                print(freeze)

def main():
    running = True
    dice = dc.roll(None, None)

    #player_list = player_create()
    p1 = player.Player("Player 1")
    turns = 0
    # Initialize board
    freeze = [0,0,0,0,0]
    start()
    rolls = 3

    while running or turns < 13:
    #for i in range(0,len(player_list)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                # Start game
                if event.key == pygame.K_r:
                    if rolls > 0:
                        rolls -= 1
                        dice = dc.roll(dice, freeze)
                        dice_roll(p1, dice, freeze, rolls)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Select Dice
                x,y = event.pos
                dice_freeze(x, y, dice, freeze, p1)
        #turns += 1    

        pygame.display.flip()
        # Constrain FPS
        clock.tick(FPS)
    
    # End of game slide

    end(player_list)

    # End Game via entering a key

if __name__=='__main__':
    main()
