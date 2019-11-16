import sys

board = [["-", "-", "-"] for x in range(3)]
players = {}

def add_symbol(symbol, position):
    row, column = position[0], position[1]
    board[row][column] = symbol

def check_horizontal(symbol):
    rows = {0: True, 1: True, 2: True}

    for row_index in range(len(board)):
        row = board[row_index]
        for tile_index in range(len(row)):
            tile = row[tile_index]
            if tile != symbol:
                rows[row_index] = False

    return dictionary[0] or dictionary[1] or dictionary[2]


def check_diagonal(symbol):
    left = right = True

    for row in board:
      for x in range(len(row)):
        left, right = x, -x-1

        if row[left] != symbol:
          left = False

        if row[right] != symbol:
          right = False

    return left or right

def check_vertical(symbol):
    dictionary = {0: True, 1: True, 2: True}

    for row in board:
        for x in range(3):
          if row[x] != symbol:
              dictionary[x] = False

    return dictionary[0] or dictionary[1] or dictionary[2]


def display_board():
    for row in board: print(row)

while True:
    player_one_symbol = input("player one's symbol: ")
    player_one_name = input("player one's name: ")
    player_two_symbol = input("player two's symbol: ")
    player_two_name = input("player two's name: ")

    if player_one_symbol != player_two_symbol:
        players = {player_one_symbol: player_one_name, player_two_symbol: player_two_name}
        break
    else:
        print("You cannot have the same symbol, pick again!")

display_board()

while True:

    for symbol, player in zip(players.keys(), players.values()):
        print("It is " + player + "'s turn...")
        while True:
            row = input("Row: ")
            column = input("Column: ")

            try:
              row = int(row)
              column = int(column)
            except ValueError:
              print("Not a valid row or column! Pick again...")
              continue


            if board[row][column] == "-":
                add_symbol(symbol, [row, column])
                display_board()
                vertical = check_vertical(symbol)
                horizontal = check_horizontal(symbol)
                diagonal = check_diagonal(symbol)

                if vertical or horizontal or diagonal:
                    print(player + " won!")
                    sys.exit()
                else:
                  break

            else:
                print("Your opponent has already picked this tile! Pick again...")