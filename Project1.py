game_list = [0,1,2]

def display_game(game_list):
    print("This is your current list")
    print(game_list)

def position_choice():
    choice = 'wrong'

    while choice not in ['0','1','2']:
        choice = input("pick a number : 0 , 1 , 2 ")
        if choice not in ['0','1','2']:
            print("sorry invalid choice")

    return int(choice)

position_choice()
