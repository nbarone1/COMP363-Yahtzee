import random as rand

def roll(dice, freeze):
    '''Roll dice. list of ints where position represents a die and value represents the number rolled (numbers must be 1-6). Defaults to rolling a random number 1-6. Set desired dice to its current value to "freeze"

    Params:
        dice: array of rand ints
        freeze: array of positions to 1-5 to freeze
    '''
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
            if f != 0:
                diceroll[f-1] = dice[f-1] 
    return diceroll
