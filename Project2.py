def player_choice():
    choice1 = ''
    while  choice1 not in ['X',"O"]:
        choice1 = input("You wanna be 'X' or 'O'")
        if choice1 not in ['X','O']:
            print("please choose X or O")
    return choice1

def player():
    if choice1 == 'X':
        choice2 = 'Y'
    else:
        choice2 = 'X'
