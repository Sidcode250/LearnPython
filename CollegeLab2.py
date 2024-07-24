from array import *
N = int(input("Number of students"))
library = []
marks = []
for i in range(N):
    Name = input("Name of student:")
    mrks = int(input("Enter Marks:"))
    library.append((Name,mrks))
    marks.append(mrks)
print(library)
print(f"average marks : {sum(marks)/N}")
print(f"Higesht marks : {max(marks)}")
print(f"Lowest marks : {min(marks)}")