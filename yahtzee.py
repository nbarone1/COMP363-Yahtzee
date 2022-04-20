import random as rand
import scorecard as sc

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


def player_turn(player):
    # Roll up to three times
    dice = roll()
    options = {}
    rerolls = 2
    while True: 
        print('dice:\nd1 d2 d3 d4 d5')
        print(dice)
        options = sc.score(dice)
        sc.validate(options, player)
        print(f'Choices: {options}\n')

        if rerolls > 0:
            print('Enter a valid scorecard option, or choose which dice to freeze')
        else:
            print('Enter a valid scorecard option')
        pick = input()
        
        # Mark scorcard with current player selection. Update scorecard
        if pick in options.keys():
            if options[pick] and options[pick] != 0:
                print(f'"{pick}" selected')
                player[pick] = options[pick] 
                return
        elif rerolls > 0:
            freeze = list(map(int, pick.replace(',', ' ').split()))
            print(freeze)
            dice = roll(dice, freeze)
            rerolls-=1
        else:
            print("Not a valid option or no rerolls left, select a valid scorecard option")


def main():
    
    # Player 1 and 2 scorecards
    p1 = sc.scorecard() 
    p2 = sc.scorecard()
    # Current Turn
    turn = True

    # Game loop    
    while True:
        if turn:
            print("\n--------------------")
            print("Player 1's turn")
            player_turn(p1)
        else:
            print("\n--------------------")
            print("Player 2's turn")
            player_turn(p2)
        
        print("------------------------------")
        print(f'| p1: {sc.calculate_score(p1)} points |\n| p2: {sc.calculate_score(p2)} points |')
        print("------------------------------")

        turn = not turn


if __name__ == '__main__':
    main()



