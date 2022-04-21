import random as rand

# Roll dice
# Dice - list of ints where position represents a die and value represents the number rolled (numbers must be 1-6)
# d1-d5 each represent a dice
# Defaults to rolling a random number 1-6. Set desired dice to its current value to "freeze"
def roll(dice=None, freeze=None):
    diceroll = [
        rand.randint(1,6), 
        rand.randint(1,6), 
        rand.randint(1,6), 
        rand.randint(1,6), 
        rand.randint(1,6)
    ]
    # Save dice rolls you would like to keep
    if dice and freeze:
        for f in freeze:
            diceroll[f-1] = dice[f-1] 
    return diceroll

