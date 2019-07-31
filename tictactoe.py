# ----- Global Variables -----

# Game Board
board = ["-", "-", "-", 
         "-", "-", "-",
         "-", "-", "-",]

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Whos turn is it
current_player = "X"

# Display board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2]) 
  print(board[3] + " | " + board[6] + " | " + board[5]) 
  print(board[6] + " | " + board[7] + " | " + board[8]) 

# Play a game of tic tac toe
def play_game():

  # Display intial board
  display_board()

  # While the game is still going
  while game_still_going:
    
    # Handle a single turn of an arbitrary player
    handle_turn(current_player)

    # Check if the game has ended
    check_if_game_over()

    # Flip to the other player
    flip_player()
  
  # The game has ended
  if winner == "X" or winner == "O":
    print (winner + " won.")
  elif winner == None:
    print ("Tie.")

# Handle a single turn of an arbitrary player
def handle_turn(current_player):
  position = input("Choose a position from 1-9: ")
  position = int(position) - 1

  board[position] = "X"

  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():

  # Set up global vairables
  global winner


  # check row
  row_winner = check_rows()
  # check columns
  column_winner = check_columns()
  # check diagonals
  diagonal_winner = check_diagonals()

  if row_winner:
    # there was a win
    winner = row_winner()
  elif column_winner:
    # there was a win
    winner = column_winner
  elif diagonal_winner:
    # there was a win
    winner = diagonal_winner()
  else:
    # there was no win
    winner = None

  return


def check_rows():
  # Set up global variables
  
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  return


def check_columns():
  return


def check_diagonals():
  return


def check_if_tie():
  return


def flip_player():
  return 


play_game()













# board
# display board
# paly game
# handle turn
#check win
  # check rows
  # check colums
  # check diagonals
# check tie
# flip player
