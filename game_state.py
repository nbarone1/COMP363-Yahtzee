import dice as dc

class Gamestate:

   def __init__(self, players):
       self.players = players
       self.player = players[0]
       self.dice = dc.roll(None, None)
       self.freeze = [0,0,0,0,0] 
       self.rolls = 3
       self.turns = 0
       

