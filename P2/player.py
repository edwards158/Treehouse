class Player(object):

  def __init__(self, name):
    self.name = name
    self.ships = []
    self.hits = []
    self.misses = []

  def add_ship(self, ship_to_add):
    if ship_to_add.name not in [ship.name for ship in self.ships]:
        self.ships.append(ship_to_add)
    else:
        raise Exception("That ship is already in the player's list.")



  def place_ship(self, ship, origin, orientation, board_size):
  
    column, row = origin

    ship_cells = []
    is_horizontal = True

    if orientation == 'h':
      for num in range(0,ship.length):
        ship_cells.append( (column+num, row) )
      print (ship_cells[0][0], ship_cells[-1][0] )
      if ship_cells[0][0] < 1 or  ship_cells[-1][0] > 5:
        return True


    elif orientation == 'v':
      for num in range(0,ship.length):
        ship_cells.append( (column,row+num) )
      is_horizontal = False

    #print("ship cells", ship_cells)
    ship.set_cells(ship_cells, is_horizontal)
    return False


  def make_guess(self, guess_tuple, opponent):

    #try:
    #    validator.validate_guess(guess_tuple, self)
    #except ValueError as ve:
    #    raise ve

    response = ""

    for ship in opponent.ships:
        if guess_tuple in ship.cells.keys():
            self.hits.append(guess_tuple)
            ship.cells[guess_tuple] = False

            if ship.is_sunk():
                response = "You sank {}'s {}".format(
                    opponent.name, ship.name)
            return True, response

    self.misses.append(guess_tuple)
    return False, response



'''
  def map_coords(self,data):

    #res = list(data)
    #print ("data is {}".format(data))
    x = data[0]
    y = data[1]
    #print (data[0])
    

    col_map = {'a':0,'b':1,'c':2,'d':3,'e':4}
    row_map = {'1':0,'2':1,'3':2,'4':3,'5':4}

    return row_map[y],col_map[x]
    #return (1,3)

  def display_action(self,player,opponent):

    ship = ['c2','c3','c4']
    board = []
    #print (board)
    #print("   " + " ".join(board_headers)) # first prints the headers

    for array in guess:
      for data in array:
        row,col =  self.map_coords(data)
        #print(row,col)
        if data in array:
          board[row][col] = HIT
        else:
          board[row][col] = MISS

    row_num = 1
    for row in board:
        print((str(row_num).rjust(2) + " " + " ".join(row)))
        row_num += 1
'''