
SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

ALPHA = ['a','b','c','d','e']
NUMERIC = ['1','2','3','4','5']

class Ships:

  def get_locations(self):
    guess = [0]*5
    for i,v in enumerate(SHIP_INFO):
      print ("Place location of {} ({} spaces):".format(v[0],v[1]))
      choice = str(input(">"))
      choice = choice.replace(" ","")
      res = list(choice)
      if res[0] in ALPHA and res[1] in NUMERIC:
        guess[i] = (res[0],res[1])
      else:
        self.get_locations()
      print (guess)

  def is_sunk(self):
    return False



  def __init__(self):
    self.locations = self.get_locations()
    print (self.locations)
    self.sunk = self.is_sunk()

    def __str__(self):
      return 'locations {}'.format(self.locations)



