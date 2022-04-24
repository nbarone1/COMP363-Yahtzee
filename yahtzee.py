# Game run to 
from turtle import clear

from numpy import empty
import player as pl

# NS code to be worked with

def main():
    clear
    name = input("Type DONE or Enter Player Name: ")
    pnames = []
    while name != "DONE":
        pnames.append(pl.Player(name))
        name = input("Type DONE or Enter Player Name: ")
    

    # Game loop
    if len(pnames)>=1:
        game = True
        while game:
            # game goes until all players have 13 turns
            for player in pnames:
                # Current Error is in player.py game_loop
                player.game_loop()
            if pnames[0].turns == 13:
                game = False

        winningscore = 0
        winner = "name"
        for player in pnames:
            if winningscore < player.getscore():
                winner = player.name
            if winningscore == player.getscore():
                winner = winner+" tied with "+player.name

        print("The winner is "+winner+" with a score of"+winningscore)

    print("play again soon")

if __name__ == '__main__':
    main()

