# Dice class for use in Player class


import random
import numpy as np

class DiceRow:
    def __init__(self):
        # 5 dice in list
        self.dice=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
        # count rolls per turn
        self.rolls = 1

    def rollAll(self,rr=None):
        if self.rolls<4:
            if rr:
                for r in rr:
                    self.dice[r-1]=random.randint(1,6)
            self.rolls += 1

        def clear():
            self.rolls = 1