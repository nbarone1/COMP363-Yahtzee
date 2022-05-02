import pygame
import os
import sys
# Yahtzee modules
import const
import load_assets as la 
import player as pl
import game_state as gs
import dice as dc

# Init pygame
pygame.init()
#pygame.font.init()
window = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
pygame.display.set_caption("Yahtzee")
pygame.display.set_icon(la.dice_assets[5])

# Render fonts
title_label = la.base_font.render("Press 'r' to roll dice", True, (255, 255, 255))
score_label = la.base_font.render("Score:", True, (255, 255, 255))

# Clock to dictate FPS
clock = pygame.time.Clock()

# input rect
input_rect = pygame.Rect(600, 400, 140, 32)

class Yahtzee:
# Create a game state
    def __init__(self, players):
        self.players = players
        self.__set_values(players[0], 0)


    def __set_values(self, player, turns):
        '''Private function to set the default gamestate values'''
        self.player = player
        self.player_options = None
        self.dice = dc.roll(None, None)
        self.freeze = [0,0,0,0,0] 
        self.rolls = 3
        self.turns = turns 


    def __render(self):
        '''Private function to render graphics'''
        # Render text
        action_label = la.base_font.render("Press 'r' to roll dice", True, (255, 255, 255))

        # Repaint the screen
        window.blit(la.background_asset, (0, 0))
        window.blit(action_label, (const.WIDTH//2 - action_label.get_width()//2, 250))

        # Repaint scorecard
        window.blit(la.scorecard_assets['upper_section'], (25, 5))
        card_width = la.scorecard_assets['aces'].get_width()
        for i, sc in enumerate(la.scorecard_assets.values()):
            card_pos = (25, 60+(i*50))
            vbox_pos = (25+card_width, 60+(i*50))
            window.blit(sc, card_pos)
            window.blit(la.scorecard_assets['value_box'], vbox_pos)

        # Print Player's Name on Top and score below scorecard
        if self.player: 
            displayname_label = la.base_font.render(f"{self.player.name}'s Turn with {self.rolls} rolls remaining", True,(255,255,255))
            window.blit(displayname_label,(620,50))
            score_label = la.base_font.render(f"Score: {self.player.player_score}", True, (255, 255, 255))
            window.blit(score_label, (const.QUARTER_WIDTH-175, const.HEIGHT-35))

            # Render sc values        
            if self.player_options:
                scorecard = self.player.scorecard
                for i, sc in enumerate(scorecard):
                    vbox_pos = (25+card_width, 60+(i*50))
                    if scorecard[sc] > -1: 
                        score_render = la.large_font.render(f"{scorecard[sc]}", True, (255,0,0))
                        window.blit(score_render, vbox_pos) 
                    else:
                        option_render = la.large_font.render(f"{self.player_options[sc]}", True, (0,0,0))
                        window.blit(option_render, vbox_pos)

        # Paint the dice faces
        if self.dice != None and self.freeze != None:
            for i, (die, f) in enumerate(zip(self.dice, self.freeze)):
                width = (1.7+(i*0.4))*const.QUARTER_WIDTH
                height = const.MIDDLE_HEIGHT
                if f != 0:
                    pygame.draw.rect(window, (255,0,0), pygame.Rect(width-5, height-5, 103, 75))
                window.blit(la.dice_assets[die], [width, height])


    def roll_event(self):
        if self.rolls == 3:
            print(f"'{self.player.name}'s turn")
        # Decrement rolls
        if self.rolls > 0:
            self.rolls-=1
            self.dice = dc.roll(self.dice, self.freeze)
        self.player_options = self.player.player_options(self.dice)
        self.__render()


    def selection_event(self, x, y):
        '''Boolean to check if selection has been made'''
        scorecard_assets = la.scorecard_assets
        dice_assets = la.dice_assets
        # Check if dice are clicked
        for i, d in enumerate(dice_assets):
            if d != None:
                coords = ((1.7+((i-1)*0.4))*const.QUARTER_WIDTH+(const.WIDTH//28), const.MIDDLE_HEIGHT+const.HEIGHT//22)
                if d.get_rect(center=coords).collidepoint(x,y):
                    if self.freeze[i-1] != 0:
                        self.freeze[i-1] = 0
                    else:
                        self.freeze[i-1] = i
                    self.__render()
                    print(self.freeze)
        # Select an option
        for i, sc in enumerate(scorecard_assets):
            instance = scorecard_assets[sc]
            if instance != None and self.player_options != None: 
                if instance.get_rect(center=(25+instance.get_width()//2, 60+(i*50)+instance.get_height()//2)).collidepoint(x,y):
                    if sc in self.player_options.keys() and self.player.scorecard[sc] == -1:
                        print(f'"{sc}" selected')
                        self.player.scorecard[sc] = self.player_options[sc] 
                        self.player.player_score = self.player.player_score+self.player_options[sc] if self.player_options[sc] > 0 else 0
                        # Return value true if selection is made
                        return True 


    def advance_turn(self):
        '''Move to the next player's turn if a selection is made. Reset values.'''
        print(f'{self.player.name} turn over')
        # Switch to the next player
        self.turns += 1
        next_player = self.players[self.turns%len(self.players)]
        # Call set values to reset to the defaults
        self.__set_values(next_player, self.turns)
        self.__render()


def main():
    running = True

    p1 = pl.Player("Player 1")
    p2 = pl.Player("Player 2")
    #player = player_create()
    players = [p1, p2] 

    game_state = Yahtzee(players)
    # Paint title screen
    window.blit(la.title_asset,(0,0))

    while running:
        # Check for game over
        if game_state.turns > 4:
            print('placeholder')
            #end(player_list)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                # Start game
                if event.key == pygame.K_r:
                    #roll_event(player, player_options, dice, freeze, rolls)
                    game_state.roll_event()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Select Dice or a scoring option
                x,y = event.pos
                selection_made = game_state.selection_event(x, y) 
                if selection_made:
                    game_state.advance_turn()

        pygame.display.flip()
        # Constrain FPS
        clock.tick(const.FPS)


if __name__=='__main__':
    main()

