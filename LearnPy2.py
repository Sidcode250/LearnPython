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

'''
from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    #print(my_list)
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
'''

'''
def myfunc(a,b):
    if a > b:
        return a
    else:
        return b 
'''

'''
def myfunc(*args):
     print([args for args in args if args % 2 == 0])
'''

'''
def myfunc(*args):
    mylist = []
    for num in args:
        if num % 2 == 0:
            mylist.append(num)
        else:
            pass
    return mylist

myfunc(2,3,4,5,6)
'''
'''
def square(a):
    return a**2

mylist = [1,2,3,4,5]

for item in map(square, mylist):
    print(item)

print(list(map(square,mylist)))
'''
'''
def splicer(mystring):
    if len(mystring)%2 == 0:
        return "Even"
    else:
        return mystring[0]

names = ["Sid", "Kashu"]

print(list(map(splicer,names)))
'''
'''
myas = [2,4,6,8,9]
print(list(map(lambda a : a**2,myas)))
print(list(filter(lambda b : b%2 == 0,myas)))
'''
'''
x = 10
def mys():
    x = 20
    print(x)
mys()
'''
'''
def multiply(numbers): 
    num = 1 
    for i in numbers:
        num = num*i
    return num
'''
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(" ","")
    mylist = []
    str1 = str1.lower()
    for i in str1:
        if i not in mylist:
            mylist.append(i)
        else:
            pass
    mylist.sort()
    return mylist == list(alphabet)
ispangram("The quick brown fox jumps over the lazy dog")