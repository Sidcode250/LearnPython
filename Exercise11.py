'''
def master_yoda(text):
    #a = text.split()
    #new_a = text.split()[::-1]
    return " ".join(text.split()[::-1])
master_yoda("I am yoda")
'''
'''
def almost_there(n):
    if n >= 90 and n <= 110:
        return True
    elif n >= 190 and n <= 210:
        return True
    else:
        return False
'''
'''
def paper_doll(text):
    mylist = []
    for i in text:
        mylist.append(i*3)
    print("".join(mylist))
    return "".join(mylist)
paper_doll("hello")
'''
'''
def summer_69(arr):
    total_sum = 0
    in_ignore_section = False
    
    for num in arr:
        if num == 6:
            in_ignore_section = True
        elif num == 9 and in_ignore_section:
            in_ignore_section = False
        elif not in_ignore_section:
            total_sum += num
            
    return total_sum
'''
'''
def print_big(letter):
    if letter == "a":
        print("    *  ")
        print("   *  * ")
        print("  ******")
        print(" *      *")
        print("*        *")
    else:
        print("idk")
'''