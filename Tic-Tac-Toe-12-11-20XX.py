# Define the game board as a list of strings
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Define a function to display the game board


def display_board():
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

# Define a function to check if a player has won the game


def check_win():
    # Check rows
    if board[0] == board[1] == board[2] != " ":
        return True
    elif board[3] == board[4] == board[5] != " ":
        return True
    elif board[6] == board[7] == board[8] != " ":
        return True
    # Check columns
    elif board[0] == board[3] == board[6] != " ":
        return True
    elif board[1] == board[4] == board[7] != " ":
        return True
    elif board[2] == board[5] == board[8] != " ":
        return True
    # Check diagonals
    elif board[0] == board[4] == board[8] != " ":
        return True
    elif board[2] == board[4] == board[6] != " ":
        return True
    # No one has won
    else:
        return False

# Define a function to check if the game is a draw


def check_draw():
    for space in board:
        if space == " ":
            return False
    return True

# Define a function to handle a player's turn


def player_turn(player):
    # Get player's move
    move = int(input("Player " + player + ", enter your move (1-9): "))
    # Check if the move is valid
    if move < 1 or move > 9:
        print("Invalid move")
        player_turn(player)
        return                      
    # Make sure the move is valid
    while board[move - 1] != " ":
        move = int
        input("Player " + player + ", enter your move")

## start the game 
# display the game board
display_board()