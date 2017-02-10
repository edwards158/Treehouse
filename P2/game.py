from player import Player


class Game(object):
  
  def setup(self):
    self.player = Player()
      
  def __init__(self):
    self.setup()
    print (self.player)


Game()
