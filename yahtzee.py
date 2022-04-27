import enum
from gc import freeze
from numpy import full, rollaxis
import py
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
PATH = os.getcwd()
ASSET_PATH = f"{PATH}/assets"

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


aces_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/aces_label.jpg"), (QUARTER_WIDTH*0.75, HEIGHT//13))
twos_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/twos_label.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13)) 
threes_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/threes_label.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13)) 
fours_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/fours_label.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13)) 
fives_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/fives_label.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13)) 
sixes_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/sixes_label.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13)) 
upper_selection_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/upper_selection.jpg"),(QUARTER_WIDTH*0.9, HEIGHT//13)) 
tofakind_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/3ofakind.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13))
fofakind_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/4ofakind.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13))
chance_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/Chance.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13)) 
fullhouse_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/Full_House.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13)) 
lgstr_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/Lg_Straight.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13))
smstr_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/Sm_Straight.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13))
yahtzee_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/Yahtzee.jpg"),(QUARTER_WIDTH*0.75, HEIGHT//13))
value_box_sc = pygame.transform.scale(pygame.image.load(f"{ASSET_PATH}/scorecard/value_box.jpg"),(QUARTER_WIDTH*0.15, HEIGHT//13)) 

# Indexed list to reference all the faces
global dice_list
dice_list = [None, dice1, dice2, dice3, dice4, dice5, dice6]
scorecard_labels_dict ={"aces" : aces_sc, "twos": twos_sc, "threes" : threes_sc, "fours" : fours_sc, "fives" : fives_sc, "sixes" : sixes_sc,"3-kind" : tofakind_sc,"4-kind" : fofakind_sc,"full-house" : fullhouse_sc,"sm-straight" : smstr_sc,"lg-straight" :lgstr_sc,"yahzee" : yahtzee_sc,"chance" : chance_sc}

pygame.display.set_icon(dice6)
card_width = aces_sc.get_width()

# Dimensions for card labels and value box labels
card_pos = [(25,60),
            (25,110), 
            (25,160), 
            (25,210), 
            (25,260), 
            (25,310),
            (25,360),
            (25,410),
            (25,460),
            (25,510),
            (25,560),
            (25,610),
            (25,660),
            (25,710)]
value_box_pos = [(25+card_width,60),
                 (25+card_width,110),
                 (25+card_width,160), 
                 (25+card_width,210), 
                 (25+card_width,260), 
                 (25+card_width,310),
                 (25+card_width,360),
                 (25+card_width,410),
                 (25+card_width,460),
                 (25+card_width,510),
                 (25+card_width,560),
                 (25+card_width,610),
                 (25+card_width,660),
                 (25+card_width,710)] 
 


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
    
                    # get text input from 0 to -1 i.e. end
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


def refresh(dice, freeze, player_p=None, player_options=None):
    # Repaint the screen
    window.blit(background, (0, 0))
    window.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 250))

    # Repaint scorecard
    window.blit(upper_selection_sc, (25, 5))
    for i, sc  in enumerate(scorecard_labels_dict.values()):
        window.blit(sc, card_pos[i])
        window.blit(value_box_sc, value_box_pos[i])


    #window.blit(scoreboard, (25, 50))
    #if player_p != None:
        #window.blit(player_p,(620,50))

    # Paint the dice faces
    if dice != None and freeze != None:
        for i, (die, f) in enumerate(zip(dice, freeze)):
            width = (1.7+(i*0.4))*QUARTER_WIDTH
            height = MIDDLE_HEIGHT
            if f != 0:
                pygame.draw.rect(window, (255,0,0), pygame.Rect(width-5, height-5, 103, 75))
            window.blit(dice_list[die], [width, height])
            
    # Paint player options
    if player_options != None:
        window.blit(player_options, (QUARTER_WIDTH*2 - player_options.get_width()//2, HEIGHT//2+100))


# Returns options
def dice_roll(player, dice, freeze,rolls):
    options = player.player_options(dice)
    print(options)
    # Print Player's Name on Top
    player_p = base_font.render(f"{player.name}'s Turn with {rolls} rolls remaining", True,(255,255,255))
    # Edit options label to current options
    player_options = options_font.render(f"Options: {options}", True, (255, 255, 255))
    refresh(dice, freeze, player_p, player_options)
    return options

    

def dice_freeze(x, y, dice, options, freeze, player):
    # Check if dice are clicked
    for i, d in enumerate(dice_list):
        if d != None:
            coords = ((1.7+((i-1)*0.4))*QUARTER_WIDTH+(WIDTH//28), MIDDLE_HEIGHT+HEIGHT//22)
            if d.get_rect(center=coords).collidepoint(x,y):
                if freeze[i-1] != 0:
                    freeze[i-1] = 0
                else:
                    freeze[i-1] = i
                refresh(dice, freeze, player)
                print(freeze)
    # Select an option
    for i, sc in enumerate(scorecard_labels_dict):
        instance = scorecard_labels_dict[sc]
        if instance != None and options != None: 
            if instance.get_rect(center=(card_pos[i][0]+instance.get_width()//2, card_pos[i][1]+instance.get_height()//2)).collidepoint(x,y):
                if sc in options.keys() and player.scorecard[sc] == -1:
                    print(f'"{sc}" selected')
                    player.scorecard[sc] = options[sc] 
                    player.player_score += options[sc]
                    return

def main():
    running = True
    dice = dc.roll(None, None)
    options = None

    p1 = player.Player("Player 1")
    p2 = player.Player("Player 2")
    #player_list = player_create()
    player_list = [p1, p2] 
    turns = 0
    # Initialize board
    freeze = [0,0,0,0,0]

    #intro = base_font.render("Press 'r' to begin the game",True,(255,255,255))
    start()

    rolls = 3
    print(f"{player_list[0].name}'s turn")
    refresh(dice, freeze)

    while running or turns < 13:
        for p in player_list:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    # Start game
                    if event.key == pygame.K_r:
                        if rolls > 0:
                            rolls -= 1
                            dice = dc.roll(dice, freeze)
                            options = dice_roll(p, dice, freeze, rolls)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Select Dice
                    x,y = event.pos
                    dice_freeze(x, y, dice, options, freeze, p)
                    print(f"{p.name}'s turn")
                    refresh(dice=None, freeze=None)
                    break

            pygame.display.flip()
            # Constrain FPS
            clock.tick(FPS)
        turns += 1    

    # end(player_list)

    # End Game via entering a key

if __name__=='__main__':
    main()
