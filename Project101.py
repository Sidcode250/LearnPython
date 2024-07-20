from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']

display_board(test_board)

def player_marker():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1 : X or O").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
player_1 , player_2 = player_marker()

print(player_1)