ALPHA = ['a','b','c','d','e']
NUMERIC = ['1','2','3','4','5']

class Display(object):

  VERTICAL_SHIP = '|'
  HORIZONTAL_SHIP = '-'
  EMPTY = 'O'
  MISS = '.'
  HIT = '*'
  SUNK = '#'


  def clear_screen(self):
    print("\033c", end="")


  def __init__(self, board_size=10):
      self.BOARD_SIZE = board_size


  def get_names(self):
    ''' get the players names
    '''

    self.clear_screen()

    players = [0]*2
    while True:
      players[0] = input("Player 1 enter your name:")
      if players[0] == "":
        print("you did not enter a name, try again")
        continue
      while True:
        players[1] = input("Player 2 enter your name:")
        if players[1] == "":
          print("you did not enter a name, try again")
          continue
        else:
          break
      break

    return players

  def starter_board(self):
    #creating the headers for the board
    board_headers=[chr(c) for c in range(ord('A'), ord('A') + self.BOARD_SIZE)]
    # crating a 2 D array of empty postion strings i.e [[row],[col]]
    board= [[self.EMPTY for c in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
    #print (board)
    #board_headers = 1;board = 2
    return board_headers, board


  def print_board_heading(self):
      print("   " + " ".join([chr(c)
                              for c in range(ord('A'), ord('A') + self.BOARD_SIZE)]))


  def print_board(self, board):
    self.print_board_heading()

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1
    print()

    # prompts the user for a series of inputs
    # returns a tuple: (input_string, orientation_string)
    # validation takes place outside
  def prompt_for_ship_placement(self, ship_to_place):
    print("Next ship: {}, Length: {}".format(
          ship_to_place.name, ship_to_place.length))

    while True:
      choice = str(input(">"))
      location = list(choice.replace(" ",""))
      if location[0].lower() not in ALPHA or location[1] not in NUMERIC:
          print("Sorry, enter 'a'-'e' then '1'-'5'.")
          continue
      break

    while True:
      print ("Is it [h]orizontal or [v]ertical:")
      orientation = input(">").lower()
      if orientation not in ('h','v'):
          print("Sorry, not correct, enter 'h' or 'v'")
          continue
      break

    column = ord(location[0]) - ord('a') + 1
    res = (column, int(location[1]))
    #print (res, location[1])

    return (res, orientation)

  def prompt_for_placement(self, ship_to_place):
    print("Enter coordinates:")

    while True:
      choice = str(input(">"))
      location = list(choice.replace(" ",""))
      if location[0].lower() not in ALPHA or location[1] not in NUMERIC:
          print("Sorry, enter 'a'-'e' then '1'-'5'.")
          continue
      break

    column = ord(location[0]) - ord('a') + 1
    res = (column, int(location[1]))
    #print (res, location[1])

    return (res)


  def construct_player_board(self, player, opponent, show_ships=True):

      board = []

      for row in range(1, self.BOARD_SIZE + 1):

          output_list = []

          for col in range(1, self.BOARD_SIZE + 1):

              icon = self.EMPTY

              if show_ships:
                  # printing player's own board
                  # show ships and opponent's hits and misses
                  for ship in player.ships:
                     # print (ship.cells.keys())
                      if (col, row) in ship.cells.keys():
                          # hit, ship, or sunk
                          if ship.is_sunk():
                              icon = self.SUNK
                          elif (col, row) in opponent.hits:
                              icon = self.HIT
                          else:
                              # ship
                              if ship.is_horizontal:
                                  icon = self.HORIZONTAL_SHIP
                              else:
                                  icon = self.VERTICAL_SHIP
                      else:
                          # miss or empty
                          if (col, row) in opponent.misses:
                              icon = self.MISS

              else:
                  # printing opponent's board
                  # show player's hits and misses
                  for ship in opponent.ships:
                      if (col, row) in ship.cells.keys():
                          if ship.is_sunk():
                              icon = self.SUNK
                          elif (col, row) in player.hits:
                              icon = self.HIT
                      else:
                          if (col, row) in player.misses:
                              icon = self.MISS

              output_list.append(icon)

          #print (output_list)
          board.append(output_list)

      return board

  def prompt_for_switch(self, opponent):

      while input("Now hand the computer to {}. Press [ENTER] when ready...".format(opponent)) != '':
          print("You should only press the [ENTER] key and nothing else!!!")

  # returns the tuple of the player's guess
  def prompt_for_guess(self):

    guessed = False

    #while not guessed:
        #try:
    guess = self.prompt_for_placement(
                "What cell would you like to guess? ")
        #except ValueError as ve:
        #    print(ve)
        #    continue

      #guessed = True

    return guess






