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
'''
#a = (1,2,3,3)
#print(len(a))
'''
a = int(input("input a number"))
if a >= 0:
    print("positive")
else:
    print("negative")
'''
'''
first_name = ('a','b','c')
last_name = ('d','e','f')
age = (20,30,40)
res = zip(first_name,last_name,age)
res = tuple(res)
#print(res)

res2 = tuple(first_name + last_name + age) 
print(res2)
'''
# find tuples with positive elemnts in list of tupples
tup = [(1,2,3), (4,5,6), (-7,8,9)]
emptytup = []
for tup1 in tup:
    if all(i>0 for i in tup1):
        emptytup.append(tup1)
    else:
        pass
print(emptytup)

