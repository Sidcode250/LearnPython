'''
def lesser_of_two_evens(a,b):
        if a < b:
            return a
        elif b < a:
            return b

def greater_of_two_odds(a,b):
        if a > b:
            return a
        elif b > a:
            return b

def check(a,b):
    x = lesser_of_two_evens(a,b)
    y = greater_of_two_odds(a,b)
    if a and b % 2 == 0:
        return x
    elif a or b % 2 == 1:
        return y
    else:
        pass
check(1,2)
'''
'''
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 ==0:
        print(min(a,b))
        return min(a,b)
    else:
        print(max(a,b))
        return max(a,b)
lesser_of_two_evens(2,5)
'''

'''
def animal_crackers(text):
    a1 = text.split()
    print(a1)
    if a1[0][0] == a1[1][0]:
        return True
    else:
        return False
animal_crackers('Levelheaded Llama')
'''
'''
def makes_twenty(a,b):
    if a + b == 20 or a == 20 or b == 20:
        return True
    else:
        return False
'''
'''
def old_macdonald(name):
    if name>3:
        return name[0].capitalize() + name[3].capitalize
    else:
        return 'name is too short'
'''
name = "siddharth"
print(name.upper())