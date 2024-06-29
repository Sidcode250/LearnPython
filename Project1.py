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

def replacement_choice(game_list,position):
    user_placement = input("entee a string to to enter")
    game_list[position] = user_placement
    return game_list

def gameon_choise():
    choice = 'wrong'

    while choice not in ['Y','N']:
        choice = input("pick Y or N")
        if choice not in ['Y' or 'N']:
            print("please choose Y or N")
    
    if choice == 'Y':
        return True
    else:
        return False
    
game_on = True

while game_on == True:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list,position)
    display_game(game_list)
    game_on = gameon_choise() 