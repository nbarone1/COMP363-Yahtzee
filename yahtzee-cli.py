import player
import dice

# Mark scorcard with current player selection. Update scorecard
def gameloop(player, dice, rerolls=2):
    # Calculate options based on roll
    print('dice:\nd1 d2 d3 d4 d5')
    print(dice)
    options = player.player_options(dice)
    print(f'Choices: {options}\n')

    if rerolls > 0:
        print('Enter a valid scorecard option, or choose which dice to freeze')
    else:
        print('Enter a valid scorecard option')
    pick = input()

    # Base case
    # Mark scorcard with current player selection. Update scorecard
    if pick in options.keys():
        if player.scorecard[pick] == 0:
            print(f'"{pick}" selected')
            player.scorecard[pick] = options[pick] 
            player.player_score += options[pick]
    elif pick == "":
        print("Pass")
    elif rerolls > 0:
        freeze = list(map(int, pick.replace(',', ' ').split()))
        print(freeze)
        dice = dice.roll(dice, freeze)
        rerolls-=1
        gameloop(dice, player, rerolls)     
    else:
        print("Not a valid option or no rerolls left, select a valid scorecard option")
        gameloop(dice, player, rerolls)     


def main():
    # Player 1 and 2 scorecards
    p1 = player.Player("Player 1") 
    p2 = player.Player("Player 2")
    # Maximum of 13 turns
    turn_limit = 1

    # Game loop    
    while turn_limit <= 1:
        print("+----------+")
        print(f"|  Turn {turn_limit}  |")
        print("+----------+")

        print("\n--------------------")
        print("Player 1's turn")
        gameloop(p1, dice.roll())

        print("\n--------------------")
        print("Player 2's turn")
        gameloop(p2, dice.roll())
        
        print("------------------------------")
        print(f'| p1: {p1.player_score} points |\n| p2: {p2.player_score} points |')
        print("------------------------------")

        turn_limit+=1

    winner = p1.name if p1.player_score > p2.player_score else p2.name 
    print("+----------+----------+----------+")
    print(f"| GAME OVER, {winner} WINS! |") 
    print("+----------+----------+----------+")


if __name__ == '__main__':
    main()



