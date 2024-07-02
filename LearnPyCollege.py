'''
a = [1,2,3,4]

def multiply(list1):
    multi = 1
    for int in list1:
        multi = multi*int
    print(multi)
    return multi

multiply(a)
'''
'''
l1 = [1,2,3,4,5,6,7]
even = l1[2:7:2]
odd = l1[1:7:2]
print(even)
print(odd)
'''
'''
l1 = [1,2,3,4,5,6,7]

def func(list1,b):
    even = []
    odd = []
    b = list1.index(int)
    for int in list1:
        if list1.index(int) % 2 == 0:
            even = even.append(int)
        else:
            odd = odd.append(int)
'''
l1 = [1,2,-3,4,-5,6]
positive = []
negative = []
for a in l1:
    if a>0:
        positive.append(a)
    elif a == 0:
        pass
    else:
        negative.append(a)
print(positive,negative) 