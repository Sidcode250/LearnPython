def player_input():
    marker = input("Enter X or O:").upper()
    while marker not in ['X','O']:
        marker = input("Enter X or O").upper()

    if marker == 'X':

        return ('X','O')
    else:
        return ('O','X')
player1_marker , player2_marker = player_input()
print(player1_marker,player2_marker)