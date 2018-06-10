from IPython.display import clear_output
from random import randint

def print_board(board):
    clear_output()
    print(" -----------------------")
    print("|{0:<6} | {1:^5} | {2:>6}|".format(" "," "," "))
    print("|   {0:<2}  | {1:^5} | {2:>3}   |".format(board[1],board[2],board[3]))
    print("|{0:<6} | {1:^5} | {2:>6}|".format(" "," "," "))
    print("|{0:-<8}-{1:-^8}-{2:->5}|".format("-","-","-"))
    print("|{0:<6} | {1:^5} | {2:>6}|".format(" "," "," "))
    print("|   {0:<2}  | {1:^5} | {2:>3}   |".format(board[4],board[5],board[6]))
    print("|{0:<6} | {1:^5} | {2:>6}|".format(" "," "," "))
    print("|{0:-<8}-{1:-^8}-{2:->5}|".format("-","-","-"))
    print("|{0:<6} | {1:^5} | {2:>6}|".format(" "," "," "))
    print("|   {0:<2}  | {1:^5} | {2:>3}   |".format(board[7],board[8],board[9]))
    print("|{0:<6} | {1:^5} | {2:>6}|".format(" "," "," "))
    print(" -----------------------")
    print("\n\nNote:\nthe order of the board is like this\n\n|1 2 3|\n|4 5 6|\n|7 8 9|\n")
    
def player_input():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Please select between X or O\n").upper()
    if marker == "X":
        return ("X","O")
    else:
        return ("O","X")

def place_marker(board,marker,position):
    board[position] = marker
    print_board(board)

def win_check(board,marker):
    return ((board[1] == board[2] == board[3] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[7] == board[8] == board[9] == marker) or
    (board[1] == board[5] == board[9] == marker) or
    (board[3] == board[5] == board[7] == marker) or
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[3] == board[6] == board[9] == marker))

def choose_first():
    randomNum = randint(0,1)
    if randomNum == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_free_check(board,position):
    if board[position] == " ":
        return True
    else:
        return False
    
def full_board_check(board):
    for i in range(1,10):
        if space_free_check(board,i):
            return False
    else:
        return True
            
def player_choice(board):
    position = 0
    while position not in range(1,10) or not(space_free_check(board,position)):
        position = int(input("Enter the position of the marker on the board [1-9]:\n"))
    return position

def replay():
    continue_playing = ""
    while continue_playing != "yes" and continue_playing != "no":
        continue_playing = input("Dou you want to continue playing? [yes/no]:\n").lower()
    if continue_playing == "yes":
        return True
    else:
        return False

    
print("Welcome to the Tic Tac Toe game in Python\n\n\n")


while True:
    board = [" "]*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn+" will go first...")
    play_game = ""
    while play_game != "yes" and play_game != "no":
        play_game = input(turn+" are you ready to play? [yes/no]:\n").lower()
    if play_game == "yes":
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == "Player 1":
            print_board(board)
            position = player_choice(board)
            place_marker(board,player1_marker,position)
            if win_check(board,player1_marker):
                print_board(board)
                print("PLAYER 1 HAS WON!!")
                break
            else:
                turn = "Player 2"
        else:
            print_board(board)
            position = player_choice(board)
            place_marker(board,player2_marker,position)
            if win_check(board,player2_marker):
                print_board(board)
                print("PLAYER 2 HAS WON!!")
                break
            else:
                turn = "Player 1"
            
        
    if not replay():
        break