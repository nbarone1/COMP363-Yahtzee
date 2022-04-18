import random as rand
import scorecard as sc

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

def game_loop(player):
    #points = 0
    dice = roll()
    print('dice: ', dice)

    options = sc.score(dice)
    print(options, "\n")
    sc.validate(options, player)
    print(f'Choices: {options}\n')
    
    pick = input()
    # Mark scorcard with current player selection. Update scorecard
    if options[pick] != 0:
        print(f'"{pick}" selected')
        #points += options[pick]
        player[pick] = options[pick] 


def main():
    
    # Player 1 and 2 scorecards
    p1 = sc.scorecard() 
    p2 = sc.scorecard()
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
       
        print(f'p1: {sc.calculate_score(p1)} points\np2: {sc.calculate_score(p2)} points')

        turn = not turn


if __name__ == '__main__':
    main()



