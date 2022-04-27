
class Player:
    
    def __init__(self, name):
        self.name = name
        self.player_score = 0
        self.scorecard = self.gen_scorecard()

    def gen_scorecard(self):
        return  { 
            "aces" : -1, 
            "twos" : -1,
            "threes" : -1,
            "fours" : -1,
            "fives" : -1,
            "sixes" : -1,
            "3-kind" : -1,
            "4-kind" : -1,
            "full-house" : -1,
            "sm-straight" : -1,
            "lg-straight" : -1,
            "yahtzee" : -1, 
            "chance" : -1
        }

    def gen_optioncard(self):
        return  { 
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
            "yahtzee" : 0, 
            "chance" : 0
    }
      
    # Valid option if it is not in current player's scorecard
    def validate(self, options):
        # Marks the current player's scorecard
        for category in self.scorecard:
            if not (self.scorecard[category] == -1 and options[category] > -1): 
                options.pop(category)
        return options


    def player_options(self, dice):
        # List of possible scores the player could take
        options = self.gen_optioncard()
        # Values - represents the count of each values; position is the dice value, 
        # value is the number of roles (Values must add up to 5, should be the case if dice len is 5)
        values = [0,0,0,0,0,0]
        for die in dice:
            values[die-1] += 1
        #print(f'debug counts of dice: {values}')
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
            if v == 5:
                options['yahtzee'] = 50
            
            options['chance'] = total
        
        # Return valid dict of options
        return self.validate(options) 

