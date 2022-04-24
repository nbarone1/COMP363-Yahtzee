# Player class for Game loop

from ast import Assign
from cmath import pi
from numpy import empty
import dice
import scorecard


class Player:
    def __init__(self,name):
        # give players name for visuals
        self.name = name
        # operate in groups of 5 die instead of individuals
        self.dice = dice.DiceRow()
        # create scorecard instance
        self.sc = scorecard.Scorecard()
        self.optioncard = scorecard.Scorecard()
        # 13 turns a game, track here
        self.turns = 0

    def getscore(self):
        return self.sc.score()

    def endturn(self):
        self.turns += 1

    def roll(self):
        self.dice.rollAll()

    def options(self):
        # List of possible scores the player could take
        options = self.optioncard.scorecard
        # Values - represents the count of each values; position is the dice value, 
        # value is the number of roles (Values must add up to 5, should be the case if dice len is 5)
        values = [0,0,0,0,0,0]
        for die in range(1,6):
            values[self.dice.getval(die)-1] += 1

        print(f'debug counts of dice: {values}\n')
        total = 0 
        # Upper section scoring
        upper_sect = list(options.keys())[:6]
        for i, val in enumerate(upper_sect):
            options[val] = values[i]*(i+1) 
            total += values[i]*(i+1) 

        # Lower section scoring
        two = three = False
        straight = 0
        for v in values:

            # Two of a kind (nothing by itself)
            if v == 2:
                two = True

            # Three of a kind
            if v == 3:
                three = True
                options['3-kind'] = total 

            # Four of a kind
            if v == 4:
                options['4-kind'] = total 

            # Full house
            if two and three:
                options['full-house'] = 25 

            # Straight count for large and small straight
            straight = straight+1 if v >= 1 else 0

            # Small straight
            if straight == 4:
                options['sm-straight'] = 30

            # Large straight
            if straight == 5:
                options['lg-straight'] = 40
        
            # Yahtzee!
            if v == 6:
                options['yahtzee'] = 50
        
        return options

    # act of taking a turn

    def game_loop(self):
        # roll, has safe guard built in dice
        self.dice.rollAll()
        dierolls = "dice:  "
        for i in range(1,6):
            dierolls = dierolls+" "+str(self.dice.getval(i))
        
        print(dierolls)

        # find options based on roll
        options = self.options()
        print(options, "\n")

        choice = int(input("Select Die to freeze from 1-5, or press 0 to skip: "))
        freezie = []
        while choice != 0:
            freezie.append(choice)
            choice = int(input("Select Die to freeze from 1-5, or press 0 to skip: "))
        if len(freezie)>0:
            for i in freezie:
                self.dice.freezeDie(i)

        for i in range(0,5):
            print(self.dice.dice[i].state)
        
        # choose what to do with result
        pick = input("Enter score choice, skip to forgo a score, or enter roll to reroll: ")
        if pick == "roll":
            self.game_loop()
            # dice will not change after a third time
        # Mark scorcard with current player selection. Update scorecard
        
        if pick != "roll":
            print(f'"{pick}" selected')
            # double check scoring

            if pick != "skip":
                if self.sc.scorecard.get(pick)==0:
                    self.sc.points += options.get(pick)
                    # tracking via boolean
                    self.sc.scorecard[pick] = 1
                else:
                    # if check fails try again
                    print("already used that row")
                    self.game_loop()

        # count turns
        self.endturn()
        self.dice.clearAll()

        # print update
        print(self.name+" has a score of "+str(self.getscore())+" after "+str(self.turns)+" turns. \n")