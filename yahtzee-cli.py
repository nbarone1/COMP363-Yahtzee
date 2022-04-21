import random as rand
import player
import dice

def main():
    # Player 1 and 2 scorecards
    p1 = player.Player("Player 1") 
    p2 = player.Player("Player 2")
    # Maximum of 13 turns
    turn_limit = 1
    turn = True

    # Game loop    
    while turn_limit <= 1:
        print("+----------+")
        print(f"|  Turn {turn_limit}  |")
        print("+----------+")

        print("\n--------------------")
        print("Player 1's turn")
        p1.gameloop(dice.roll())

        print("\n--------------------")
        print("Player 2's turn")
        p2.gameloop(dice.roll())
        
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



