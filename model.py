# Model for Yahtzee Game

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

class Scorecard:
    def __init__(self):
        self.score = 0
        self.card = np.zeros(13, dtype = int)
    
    def one():
        if card[0] == 0:                    
            n = 0
            for i in dice:
                if i.value == 1:
                    n = n+1
            card[0] = n*1
        
    def two():
        if card[1] == 0:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            card[1] = 2*n
    
    def three():
        if card[2] == 2:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            card[2]=3*n