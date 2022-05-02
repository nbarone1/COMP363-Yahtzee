'''Load game assets'''
import pygame
import const


def __init_dice():
    dice_assets = [None]
    for i in range(1,7):
        dice_assets.append(pygame.transform.scale(pygame.image.load(f"{const.ASSET_PATH}/dice{i}.jpg"), (const.WIDTH//14, const.HEIGHT//12)))
    return dice_assets

def __init_scorecard():
    scorecard_assets = {
            "aces" : None, 
            "twos": None, 
            "threes" : None, 
            "fours" : None, 
            "fives" : None, 
            "sixes" : None,
            "3_kind" : None,
            "4_kind" : None,
            "full_house" : None,
            "sm_straight" : None,
            "lg_straight" :None,
            "yahtzee" : None,
            "chance" : None 
    }
    for label in scorecard_assets:
        scorecard_assets[label] = pygame.transform.scale(pygame.image.load(f"{const.ASSET_PATH}/scorecard/{label}.jpg"), (const.QUARTER_WIDTH*0.75, const.HEIGHT//13))
    scorecard_assets['value_box'] = pygame.transform.scale(pygame.image.load(f"{const.ASSET_PATH}/scorecard/value_box.jpg"),(const.QUARTER_WIDTH*0.15, const.HEIGHT//13))  
    scorecard_assets['upper_section'] = pygame.transform.scale(pygame.image.load(f"{const.ASSET_PATH}/scorecard/upper_section.jpg"),(const.QUARTER_WIDTH*0.9, const.HEIGHT//13)) 
    return scorecard_assets


# INITS
# --------------------
dice_assets = __init_dice()
scorecard_assets = __init_scorecard()
# Game Background,
background_asset = pygame.transform.scale(pygame.image.load(f"{const.ASSET_PATH}/gameboard.jpg"), (const.WIDTH, const.HEIGHT))
# Scorecard
scoreboard_asset = pygame.transform.scale(pygame.image.load(f"{const.ASSET_PATH}/scorecard.png"), (const.QUARTER_WIDTH, const.MIDDLE_HEIGHT*1.75))
# Start/end slides
title_asset = pygame.transform.scale(pygame.image.load(f"{const.ASSET_PATH}/title_screen.jpg"), (const.WIDTH, const.HEIGHT))
gameover_asset = pygame.transform.scale(pygame.image.load(f"{const.ASSET_PATH}/game_over.jpg"), (const.WIDTH, const.HEIGHT))

# Fonts and text
pygame.font.init()
base_font = pygame.font.SysFont("courier new", 24)
s_font = pygame.font.SysFont("courier new", 36)
med_font = pygame.font.SysFont("courier new", 24)
options_font = pygame.font.SysFont("courier new", 10)

#print(dice_assets)
#print('\n', scorecard_assets)
