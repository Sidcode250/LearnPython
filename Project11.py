def display_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6]) 
    print(board[1] + "|" + board[2] + "|" + board[3])

test_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X", "O"]
'''
def player_input():
    marker = input("Player 1 enter X or O:").upper()
    while marker not in ['X','O']:
        marker = input("Player 1 enter X or O:").upper()
    if marker == 'X':
        return ("X","Y")
    else:
        return ("Y","X")
'''
def player_input():
    marker = input("Enter X or O:").upper()
    while marker not in ['X','O']:
        marker = input("Enter X or O").upper()
    print(marker)
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
player1_marker , player2_marker = player_input()