#Functions 

'''
def func_name(name):
    print("Hello " + name)
func_name('Sid')
'''

'''
def fun_add(a,b):
    print(a+b)
fun_add(2,3)
'''

'''
def say_hello(name):
    print(f"Hello {name}")
say_hello("Siddharth")
'''

'''
def even(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
even(26)
''' 

'''
def fun2(list):
    for num in list:
        if num % 2 == 0:
            print(num,"= Even")
        else:
            print(num,"= Odd")
fun2([2,4,5,7,9,10])
'''

'''
def even_list(list):
    empty_list = []
    for num in list:
        if num % 2 == 0:
            empty_list.append(num)
        else:
            pass
    print(empty_list)
even_list([2,5,7,10])
'''


from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    print(my_list)
    return my_list

def guess_a():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("pick a number: 0,1,2")
    return int(guess)

def check(my_list, guess):
    if my_list[guess] == 'o':
        print("right")
    else:
        print("wrong")

game = [' ', 'o', ' ']
game1 = shuffle_list(game)
game2 = guess_a()
check(game1,game2)