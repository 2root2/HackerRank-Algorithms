from __future__ import print_function
from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print('  '+board[0]+ ' | '+board[1]+' | '+board[2])
    print('--------------')
    print('  '+board[3]+ ' | '+board[4]+' | '+board[5])
    print('--------------')
    print('  '+board[6]+ ' | '+board[7]+' | '+board[8])

def win_check(board, mark):
    return ((board[6] == mark and board[7] == mark and board[8] == mark) or # across the top
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
    (board[0] == mark and board[1] == mark and board[2] == mark) or # across the bottom
    (board[6] == mark and board[3] == mark and board[0] == mark) or # down the middle
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the right side
    (board[6] == mark and board[4] == mark and board[2] == mark) or # diagonal
    (board[8] == mark and board[4] == mark and board[0] == mark)) # diagonal

def place_marker(board, marker, position):
    board[position-1] = marker

def space_check(board, position):
    return board[position-1] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def random_turn():
    return random.randint(1,2)

def next_player(current_player):
    if current_player == 1:
        return 2
    else:
        return 1

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want to choose X or O :').upper()
    
    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

def player_choice():
    position = ''
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input("Choose your position 1-9 :")
    return int(position)

def replay():
    return raw_input("Do you want to play again> Yes(Y) No (N)").lower().startswith('y')

def get_player_marker(player1_marker, player2_marker, player):
    if(player == 1):
        return player1_marker
    else:
        return player2_marker

while True:
    board = [' '] *10
    player1_marker, player2_marker = player_input() #marker Choice
    current_player = random_turn()
    print('Player '+str(current_player)+' will go first')

    game_on = True

    while game_on:
        display_board(board)
        position = player_choice()
        print (position)
        marker = get_player_marker(player1_marker, player2_marker, current_player)
        place_marker(board, marker, position)

        if win_check(board, marker):
            display_board(board)
            print("Congratualations Player "+ str(current_player)+ " has won the match")
            break;
        else:
            if full_board_check(board):
                display_board(board)
                print("It's a draw")
                break;
            else:
                print("player "+ str(next_player(current_player))+", Marker : "+str(get_player_marker(player1_marker, player2_marker,next_player(current_player))) +".")
                current_player = next_player(current_player)
            pass

    if not replay():
        break;