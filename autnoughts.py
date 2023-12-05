import random

def print_board(board):
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("___|___|___")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("___|___|___")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print(" | | ")

def check_winner(board, player):
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  
        [1, 5, 9], [3, 5, 7]             
    ]

    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def computer_move(board):
    available_moves = [pos for pos in range(1, 10) if board[pos] == ' ']
    return random.choice(available_moves)

def tic_tac_toe():
    board = [' '] * 10  # Using index 0 as a placeholder

    print("Tic-Tac-Toe Game")
    print("Player [X] --- Computer [O]\n")

    player = 'X'
    while True:
        print_board(board)
        
        if player == 'X':
            choice = int(input(f"Player {player}'s turn. Enter position (1-9): "))
            if board[choice] == ' ':
                board[choice] = player

                if check_winner(board, player):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                elif ' ' not in board[1:]:
                    print_board(board)
                    print("It's a draw!")
                    break
                else:
                    player = 'O'
            else:
                print("That position is already taken. Try again.")
        else:
            print("Computer's turn...")
            choice = computer_move(board)
            board[choice] = player

            if check_winner(board, player):
                print_board(board)
                print("Computer wins!")
                break
            elif ' ' not in board[1:]:
                print_board(board)
                print("It's a draw!")
                break
            else:
                player = 'X'

if __name__ == "__main__":
    tic_tac_toe()















































































# This function, print_board, takes a board as input and displays the Tic-Tac-Toe grid. It prints the current state of the game board in a user-friendly format on the console, showing positions 1 through 9. Each board position is represented by the value stored in the board list at that particular index.

# This check_winner function examines the board and determines if a player has won the game. It uses a list of winning conditions (combinations of positions that lead to a win in Tic-Tac-Toe) for rows, columns, and diagonals. It checks if any of these conditions are met by comparing the marks on the board to the current player. If a winning condition is found, it returns True; otherwise, it returns False.

# This computer_move function determines the computer's move in the Tic-Tac-Toe game. It analyzes the board to find available positions (represented by spaces ' ') by creating a list of these positions from 1 to 9. Then, it randomly selects one of these available moves using the random.choice() function and returns the chosen position for the computer's move.






# Initialization:
# board = [' '] * 10: This creates a list representing the game board. It's a 1D list with 10 elements. The first element (at index 0) isn't used for the game board, and the actual game positions are from indices 1 to 9.
# player = 'X': It sets the initial player as 'X', indicating that the game begins with the human player.

# Game Loop:
# while True:: This initiates an infinite loop that continues until a break statement is encountered, signifying the end of the game.
# print_board(board): It displays the current state of the board in the console, showing the positions and player marks.

# Player X's Turn:
# if player == 'X':: Checks if it's the human player's turn.
# choice = int(input(f"Player {player}'s turn. Enter position (1-9): ")): Prompts the human player to input their desired position on the board.
# board[choice] = player: Places 'X' at the chosen position on the board.
# Checks if Player X wins or if the game results in a draw. If either condition is met, it prints the corresponding message and exits the loop (break). Otherwise, it switches to the Computer's turn by changing player to 'O'.

# Computer O's Turn:
# if player == 'O':: Executes when it's the computer's turn.
# choice = computer_move(board): Invokes the computer_move function to determine the computer's move.
# board[choice] = player: Places 'O' at the chosen position on the board.
# Checks if Computer O wins or if the game results in a draw. If either condition is met, it prints the corresponding message and exits the loop (break). Otherwise, it switches back to Player X's turn by changing player to 'X'.

# Game Conclusion:
# If there's a winner or the game ends in a draw, it displays the final board state and the outcome of the game.





# This line ensures that the tic_tac_toe() function runs automatically only when the Python script is executed directly, allowing the game to start when the file is run as a standalone program. If this script were imported into another Python file, the tic_tac_toe() function would not execute automatically, and its functions could be used within the importing script.

 