# Dice class for use in Player class


import random
import numpy as np

class Die:
    # die to be played w, we will use 5 of these per player
    def __init__(self):
        # die has no face value yet
        self.value = 0
        # die is not frozen
        self.state = 0
        # die has 0 rolls made
        self.rolls = 0
    
    def roll(self):
        if self.state == 0:
            if self.rolls <3:
                self.value = random.randint(1,6)
                self.rolls = rolls+1
                if self.rolls == 3:
                    self.state = 1

    def freeze(self):
        if self.state == 0:
            self.state = 1
    
    def clear(self):
        self.value = 0
        self.state = 0
        self.rolls = 0

class DiceRow:
    def __init__(self):
        self.dice=[Die(),Die(),Die(),Die(),Die()]

    def clearAll(self):
        for i in range(0,5):
            self.dice[i].clear()  