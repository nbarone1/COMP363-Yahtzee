import random as rand
import scorecard as sc

def score(dice):
    # List of possible scores the player could take
    options = sc.Scorecard()
    # Values - represents the count of each values; position is the dice value, 
    # value is the number of roles (Values must add up to 5, should be the case if dice len is 5)
    values = [0,0,0,0,0,0]
    for die in dice:
        values[die-1] += 1

    print(f'debug counts of dice: {values}\n')
    total = 0 
    # Upper section scoring
    upper_sect = list(options.scorecard.keys())[:6]
    for i, val in enumerate(upper_sect):
        options.scorecard[val] = values[i]*(i+1) 
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
            options.scorecard['3-kind'] = total 

        # Four of a kind
        if v == 4:
            options.scorecard['4-kind'] = total 

        # Full house
        if two and three:
            options.scorecard['full-house'] = 25 

        # Straight count for large and small straight
        straight = straight+1 if v >= 1 else 0

        # Small straight
        if straight == 4:
            options.scorecard['sm-straight'] = 30

        # Large straight
        if straight == 5:
            options.scorecard['lg-straight'] = 40
    
        # Yahtzee!
        if v == 6:
            options.scorecard['yahtzee'] = 50
    
    return options.scorecard

# def print_state():

# Roll dice
# Dice - list of ints where position represents a die and value represents the number rolled (numbers must be 1-6)
# d1-d5 each represent a dice
# Defaults to rolling a random number 1-6. Set desired dice to its current value to "freeze"
def roll(
        d1=rand.randrange(1,7), 
        d2=rand.randrange(1,7), 
        d3=rand.randrange(1,7), 
        d4=rand.randrange(1,7), 
        d5=rand.randrange(1,7)):
    return [d1,d2,d3,d4,d5]

def validate(options, player):
    # valid option if it is not in current player's scorecard
    print
    for roll, record in zip(options, player):
        if options[record].get() != 1: 
            print(roll)
    

def game_loop(player):
    dice = roll()
    print('dice: ', dice)

    options = score(dice)
    print(options, "\n")
    #validate(options, player)
    
    pick = input()
    # Mark scorcard with current player selection. Update scorecard
    if options[pick] != 0:
        print(f'"{pick}" selected')
        player.points += options[pick]
        player.scorecard[pick] = 1


def main():
    
    # Player 1 and 2 scorecards
    p1 = sc.Scorecard() 
    p2 = sc.Scorecard()
    # Current Turn
    turn = True

    #game_loop(p1)
    

    # Game loop    
    while True:
        if turn:
            print("Player 1's turn")
            game_loop(p1)
        else:
            print("Player 2's turn")
            game_loop(p2)
        
        print(f'p1: {p1.points} points\np2: {p2.points} points')

        turn = not turn


if __name__ == '__main__':
    main()



