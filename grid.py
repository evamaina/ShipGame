"""Create a 5 x 5 grid initialized to all 'O's and store it in board.

Use range() to loop 5 times.
Inside the loop, .append() a list containing 5 "O"s to board, just like in the example above."""


board = []
for i in range(5):
	board.append(['O'] * 5)
#Using the print command to display the contents of the board list.
print board
"""define a function named print_board with a single argument, board_in.

Inside the function, write a for loop to iterates through each row in board and print it to the screen.

Call your function with board to make sure it works."""
for i in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in board:
    #print row
# inside the for loop, use " " as the separator to .join the elements of each row.    
    print " ".join(row)
print_board(board)

 