'''
def master_yoda(text):
    #a = text.split()
    #new_a = text.split()[::-1]
    return " ".join(text.split()[::-1])
master_yoda("I am yoda")
'''
def almost_there(n):
    if n >= 100 or n >= 200:
        return True
    elif n <= 100 or n <= 100:
        return True
    else:
        return False
almost_there(104)