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

    # scorecard structure to track player points
    def __init__(self):
        self.score = 0
        self.card = np.zeros(13, dtype = int)

    def getscore():
        for i in dice:
            score = score+i.value
        return score
    
    def one():
        #number of ones
        if card[0] == 0:                    
            n = 0
            for i in dice:
                if i.value == 1:
                    n = n+1
            card[0] = n*1
        
    def two():
        # number of twos
        if card[1] == 0:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            card[1] = 2*n
    
    def three():
        # number of threes
        if card[2] == 2:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            card[2]=3*n
    
    def four():
        # number of fours
        if card[3] == 0:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            card[3] = 4*n
    
    def five():
        # number of fives
        if card[4] == 0:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            card[4]=5*n
    
    def six():
        # number of sixes
        if card[5]==0:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            card[5] = 6*n
    
    def seven():
        # 3 of a kind
        if card[6] == 0:
            for i in range(1,7):
                n = 0
                for k in dice:
                    if k.value == i:
                        n = n+1
                if n >= 3:
                    sum = 0
                    for k in dice:
                        sum = sum+k.value
                    card[6]=sum

    def eight():
        # 4 of a kind
        if card[7] == 0:
            for i in range(1,7):
                n = 0
                for k in dice:
                    if k.value == i:
                        n = n+1
                if n >= 4:
                    sum = 0
                    for k in dice:
                        sum = sum+k.value
                    card[7]=sum
    def nine():
        # full house
        if card[8] == 0:
            
