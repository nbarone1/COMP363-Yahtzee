# Model for Yahtzee Game

import random

class Die:
    # die to be played w, we will use 5 of these per player
    def __init__(self):
        # die has no face value yet
        self.value = 0
        # die is not frozen
        self.state = 0
        # die has 0 rolls made
        self.rolls = 0
    
    def roll():
        if state == 0:
            if rolls <3:
                value = random.randint(1,6)
                rolls = rolls+1
                if rolls == 3:
                    state = 1

    def freeze():
        if state == 0:
            state = 1
    
    def clear():
        value = 0
        state = 0
        rolls = 0
