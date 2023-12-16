# IMPORTING MODULES
import math
import random

class TicTacToe_AI:
    def __init__(sf):  # Representing the Tic-Tac-Toe board as a list
        sf.board = [' ' for _ in range(9)]  
        sf.human_player = 'X' # HUMAN PLAYER IS 'X'
        sf.ai_player = 'O'  # AI PLAYER IS 'O'

    def print_board(sf):
        for row in [sf.board[i:i + 3] for i in range(0, 9, 3)]: # FOR LOOP FOR CREATION OF BOARD 
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(sf):
        return [i for i, spot in enumerate(sf.board) if spot == ' ']

    def empty_spots(sf):
        return ' ' in sf.board

    def board_full(sf):
        return not sf.empty_spots()

    def make_move(sf, position, player):
        sf.board[position] = player

    def check_winner(sf, player): # FUNCTION TO FIND THE 'WINNER'
        # Check rows, columns, and diagonals
        # DETERMINING THE POSSIBLE WIN SITUATIONS
        win_combs = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6)]

        for combo in win_combs:
            if all(sf.board[i] == player for i in combo):
                return True

        return False

def minimax(board, depth, maximizing_player, alpha, beta): # MIN-MAX ALGORITHM FUNCTION USING ALPHA-BETA PRUNING
    scores = {'X': -1, 'O': 1, 'TIE': 0}

    if board.check_winner('X'):
        return -1
    if board.check_winner('O'):
        return 1
    if not board.empty_spots():
        return 0

    if maximizing_player:
        max_eval = float('-inf') # DEFINING THE max_eval(ALPHA) AS -INFINITY
        for move in board.available_moves():
            board.make_move(move, 'O')
            eval = minimax(board, depth + 1, False, alpha, beta)
            board.make_move(move, ' ')
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf') # DEFINING THE min_eval(BETA) AS INFINITY
        for move in board.available_moves():
            board.make_move(move, 'X')
            eval = minimax(board, depth + 1, True, alpha, beta)
            board.make_move(move, ' ')
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board): # FUNCTION FOR BEST MOVE
    best_score = float('-inf')
    best_move = None
    for move in board.available_moves():
        board.make_move(move, 'O')
        score = minimax(board, 0, False, float('-inf'), float('inf'))
        board.make_move(move, ' ')
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def main(): # DEFINING THE MAIN FUNCTION
    game_board = TicTacToe_AI() # CALLING THE CLASS
    
    print("Welcome to AI-Tic-Tac-Toe!")
    print(f"You are '{game_board.human_player}', and the AI is '{game_board.ai_player}'. Let's play!\n")

    while not game_board.board_full():
        # Human Player's turn
        game_board.print_board()
        user_move = int(input("Enter your move(1-9): ")) - 1

        if user_move not in game_board.available_moves():
            print("Invalid move.Please Try again.")
            continue

        game_board.make_move(user_move, game_board.human_player)

        if game_board.check_winner(game_board.human_player):
            game_board.print_board()
            print("Congratulations! You win!") # HUMAN PLAYER WINS
            break

        if game_board.board_full():
            print("It's a tie!") # NO PLAYER WINS
            break

        # AI PLATER'S turn
        ai_move = best_move(game_board)
        game_board.make_move(ai_move, game_board.ai_player)

        if game_board.check_winner(game_board.ai_player):
            game_board.print_board() 
            print("AI wins! Better luck next time.") # AI PLAYER WINS
            break

    print("Game over!")

if __name__ == "__main__": # CALLING THE MAIN FUNCTION
    main()
