import art
import os
import random

def print_board(board: list[list[str]]) -> None:
    print("   0   1   2 ")
    for row in range(3):
        print(f"{row}  {board[row][0]} | {board[row][1]} | {board[row][2]} ")
        if row != 2:
            print("  ---+---+---")

def place_symbol(board: list[list[str]], position: tuple[int, int], player_symbol: str) -> None:
    board[position[0]][position[1]] = player_symbol

def is_valid_move(board: list[list[str]], position: tuple[int, int]) -> bool:
    return board[position[0]][position[1]] == " "

os.system('cls' if os.name == 'nt' else 'clear')
print(art.tic_tac_toe_art)
print("Welcome to Tic-tac-toe!")
print("Flipping a coin to see who gets to be X and goes first...")

current_player_symbol: str = "X"
is_user_turn: bool

if random.randint(0, 1) == 1:
    is_user_turn = True
    print("You are X, so you will go first!")
else:
    is_user_turn = False
    print("You are O. The computer will make the first move.")

is_game_over: bool = False
board: list[list[str]] = [[" " for j in range(3)] for i in range(3)]
did_user_win: bool

for i in range(9):
    print()

    print("The computer is choosing its play...")
    computer_play: tuple[int, int] = (random.randint(0, 2), random.randint(0, 2))
    while not is_valid_move(board, computer_play):
        computer_play: tuple[int, int] = (random.randint(0, 2), random.randint(0, 2))
    place_symbol(board, computer_play, current_player_symbol)
    print(f"It has chosen {computer_play}.")

    print()
    print_board(board)
