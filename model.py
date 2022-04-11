# Model for Yahtzee Game

from multiprocessing.sharedctypes import Value
import random
from unicodedata import name
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

class DiceRow():
    def __init__(self):
        # list of 5 die
        self = []
        for i in range(1,6):
            self.append(Die)


class Player(name):
    def __init__(self,name):
        self.name = name
        self.dice = DiceRow()
        self.scorecard = np.zeros(13, dtype = int)
        self.score = 0

    def getscore():
        return score
    
    def one():
        #number of ones
        if scorecard[0] == 0:                    
            n = 0
            for i in dice:
                if i.value == 1:
                    n = n+1
            scorecard[0] = n*1
        
    def two():
        # number of twos
        if scorecard[1] == 0:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            scorecard[1] = 2*n
    
    def three():
        # number of threes
        if scorecard[2] == 2:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            scorecard[2]=3*n
    
    def four():
        # number of fours
        if scorecard[3] == 0:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            scorecard[3] = 4*n
    
    def five():
        # number of fives
        if scorecard[4] == 0:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            scorecard[4]=5*n
    
    def six():
        # number of sixes
        if scorecard[5]==0:
            n = 0
            for i in dice:
                if i.value == 2:
                    n = n+1
            scorecard[5] = 6*n
    
    def seven():
        # 3 of a kind
        if scorecard[6] == 0:
            for i in range(1,7):
                n = 0
                for k in dice:
                    if k.value == i:
                        n = n+1
                if n >= 3:
                    sum = 0
                    for k in dice:
                        sum = sum+k.value
                    scorecard[6]=sum

    def eight():
        # 4 of a kind
        if scorecard[7] == 0:
            for i in range(1,7):
                n = 0
                for k in dice:
                    if k.value == i:
                        n = n+1
                if n >= 4:
                    sum = 0
                    for k in dice:
                        sum = sum+k.value
                    scorecard[7]=sum
    def nine():
        # full house
        if scorecard[8]==0:
            values = {}
            # dictionary of values of dice
            for i in dice:
                if i.value in values:
                    values[i.value] += 1
                else:
                    values.add(i.value)
            # adding scores based on what values have 3 and 2 appearances
            for k in values:
                k = 3
