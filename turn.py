from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row
print ship_col

for turn in range(4):
  print "Turn", turn + 1
  """ Create a new variable called guess_row and set it to int(raw_input("Guess Row: ")).
Create a new variable called guess_col and set it to int(raw_input("Guess Col: "))."""
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"   
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      """Set the list element at guess_row, guess_col to "X"and call print_board(board)"""

      board[guess_row][guess_col] = "X"
    print_board(board)


    """
Add a for loop that repeats the guessing and checking part of your game for 4 turns, like the example above.

At the beginning of each iteration, print "Turn", turn + 1 to let the player know what turn they are on."""