from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

#test_board = ['#','X','O','X','O','X','O','X','O','X']
test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#display_board(test_board)

def player_marker():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1 : X or O :").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
player_1 , player_2 = player_marker()

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    print ((board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark)
            or (board[1] == mark and board[2] == mark and board[3] == mark) or (board[7] == mark and board[4] == mark and board[1] == mark)
            or (board[8] == mark and board[5] == mark and board[2] == mark) or (board[9] == mark and board[6] == mark and board[3] == mark)
            or (board[7] == mark and board[5] == mark and board[3] == mark) or (board[9] == mark and board[5] == mark and board[1] == mark))
i = int(input("Enter Position"))
'''
def choose_position():
    inti = int(input("Enter position")) 
    return i == inti
'''
#choose_position()
place_marker(test_board,player_1,i)
display_board(test_board)
#win_check(test_board,player_1)
"""
while win_check(test_board,player_1) == True:
    choose_position()
"""