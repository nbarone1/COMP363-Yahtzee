# Player Class
class Player:
    def __init__(self):
        self.score = 0
        self.scorecard = { 
            "aces" : 0, 
            "twos" : 0,
            "threes" : 0,
            "fours" : 0,
            "fives" : 0,
            "sixes" : 0,
            "3-kind" : 0,
            "4-kind" : 0,
            "full-house" : 0,
            "sm-straight" : 0,
            "lg-straight" : 0,
            "yahtzee" : 0
        }

