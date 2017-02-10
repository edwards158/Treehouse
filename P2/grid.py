import random
from ships import Ships


SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 3

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'


board_size = 5
EMPTY = 'O'

def clear_screen():
    print("\033c", end="")


def starter_board():
    #creating the headers for the board
    board_headers=[chr(c) for c in range(ord('A'), ord('A') + board_size)]
    # crating a 2 D array of empty postion strings i.e [[row],[col]]
    board= [[EMPTY for c in range(board_size)] for _ in range(board_size)]

    return board_headers, board

def print_board(board_headers,board):
    print("   " + " ".join(board_headers)) # first prints the headers

    row_num = 1
    for mylist in board:
        #print (mylist)
        #printing out each list with a number to its right to represent the row
        print(str(row_num).rjust(2) + " " +" ".join(mylist))
        row_num += 1
    return board

def coords_to_numbers(guess):

    res = list(guess)

    x = res[0]
    y = res[1]

    print (x,y)

    x_coord = {'a':0,'b':1,'c':2,'d':3,'e':4}
    y_coord = {'1':0,'2':1,'3':2,'4':3,'5':4}

    return x_coord[x],y_coord[y]

def display_action(guess,board):

    ship = ['c2','c3','c4']
    #print (board)
    
    for place in ship:
        row,col =  coords_to_numbers(place)
        print(row,col)
        if place in guess:
            board[row][col] = HIT
        else:
            board[row][col] = MISS

    row_num = 1
    for row in board:
        print((str(row_num).rjust(2) + " " + " ".join(row)))
        row_num += 1

       
if __name__ == '__main__':

    board, board_headers = starter_board()
    board = print_board(board, board_headers)
    #guess = [('c','1'),('c','3'),('c','4')]
    #clear_screen()
    print ('\n')
    
    ship = Ships()
    print(ship.locations)

    #display_action(guess, board)


    #ship = Ships()
#ship = Grid()
#ship.starter_board()
#ship.print_board()
#user = list("e2");
#print (list(user))
#row,number = ship.coords_to_numbers(user[0],user[1])
#print (row,number)

#ship.ships = Ships()

#res = ship.ships.ship_data()
