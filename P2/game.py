from display import Display
from player import Player
from ship import Ship

class Game(object):

  BOARD_SIZE = 10

  SHIP_INFO = [
      ("Aircraft Carrier", 5),
      ("Battleship", 4),
      ("Submarine", 3),
      ("Cruiser", 2),
      ("Patrol Boat", 1)
  ]

  def __init__(self):
    self.display = Display(self.BOARD_SIZE)
    players = self.display.get_names()
    self.player_1 = Player(players[0])
    self.player_2 = Player(players[1])



  def set_up_board(self, player, opponent):
    self.display.clear_screen()


  def set_up_game(self, player, opponent):

    self.display.clear_screen()

    #board_headers, board = self.display.starter_board()
      
    #self.display.print_board(board)
    
    ship_index = 0
    
    while ship_index  < len(self.SHIP_INFO):
    # board_headers, board = self.display.starter_board()
      
    # self.display.print_board(board)

      board = self.display.construct_player_board(player, opponent, True)
      self.display.print_board(board)

      ship_name, ship_length = self.SHIP_INFO[ship_index]
      

      ship_to_add = Ship(ship_name, ship_length)

      
      player.add_ship(ship_to_add)

      origin, orientation = self.display.prompt_for_ship_placement(
                  ship_to_add)

      #print (origin, orientation)
    
      player.place_ship(ship_to_add, origin,
                                    orientation, self.BOARD_SIZE)

      #self.display.clear_screen()

      #print (player.ships)

      ship_index += 1

    self.display.prompt_for_switch(opponent.name)

    #player.add_ship(ship_to_add)
    #print (origin, orientation)
    #board = self.display.display_action(
    #  player, oppoent, True)
    #self.display.print_board(board)


  def lost(self, player):


    for ship in player.ships:
        if not ship.is_sunk():
            return False

    return True

  def play_game(self):

      player_1_turn = True

      while True:

        if player_1_turn:
            self.player_turn(self.player_1, self.player_2)

            if self.lost(self.player_2):
                print("Game Over! You sank all {}'s ships!".format(
                    self.player_2.name))
                break

            player_1_turn = False
        else:
            self.player_turn(self.player_2, self.player_1)

            if self.lost(self.player_1):
                print("Game Over! You sank all {}'s ships!".format(
                    self.player_1.name))
                break

            player_1_turn = True


  def player_turn(self, player, opponent):


    self.display.clear_screen()
    
    guess_made = False

    while not guess_made:

        print("OPPONENT'S BOARD")
        board = self.display.construct_player_board(
            player, opponent, False)
        self.display.print_board(board)

        print("YOUR BOARD [{}]".format(player.name))
        board = self.display.construct_player_board(
            player, opponent, True)
        self.display.print_board(board)

        guess = self.display.prompt_for_guess()

        #try:
        success, message = player.make_guess(guess, opponent)
       # except Exception as ve:
        self.display.clear_screen()
         #   print(ve)
         ##   print()
         #   continue

        guess_made = True

    if success:
        print("You got a hit!!!")
        if message != "":
            print(message)
    else:
        print("Bummer! You missed.")

    self.display.prompt_for_switch(opponent.name)


if __name__ == "__main__":

  fun = Game()


  fun.set_up_game(fun.player_1, fun.player_2)

  fun.set_up_game(fun.player_2, fun.player_1)

  fun.play_game()






