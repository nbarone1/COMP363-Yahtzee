import pygame
import random
import os
import player
import dice

# Constants
WIDTH = 1300
HEIGHT = 750
FPS = 60
QUARTER_WIDTH = WIDTH//4
MIDDLE_HEIGHT = HEIGHT//2
ASSET_PATH = f"{os.environ['HOME']}/github_repos/yahtzee/assets" 
               
def rollDice():
    """ Roll 5 dice """
    return [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]

def main():
    # Init game
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

    clock = pygame.time.Clock()
    running = True
    result1=result2=result3=result4=result5=None

    curr_roll = None
    while running:
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    curr_roll = dice.roll()

        # Repaint the screen
        window.blit(background, (0, 0))
        window.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 250))
        window.blit(score_label, (QUARTER_WIDTH//2 - score_label.get_width()//2, HEIGHT-40))#+ score_label.get_height()//2))
        window.blit(scoreboard, (25, 50))
        window.blit(scoreboard, (3*QUARTER_WIDTH-25, 50))
        
        # Paint the dice faces
        if curr_roll != None:
            for i, c in enumerate(curr_roll):
                window.blit(dice_list[c], ((1.3+(i*0.3))*QUARTER_WIDTH, MIDDLE_HEIGHT))
           
        # flush display changes
        pygame.display.flip()
                
        # Constrain FPS
        clock.tick(FPS)

    pygame.quit()

if __name__=='__main__':
    main()
