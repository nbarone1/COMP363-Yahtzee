# Player class for Game loop

import dice
import scorecard


class Player:
    def __init__(self,name):
        self.name = name
        self.dice = dice.DiceRow()
        self.sc = scorecard.Scorecard()
        self.turns = 0

    def getscore(self):
        self.sc.score()

    def endturn(self):
        self.turns += 1