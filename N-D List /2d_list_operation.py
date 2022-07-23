# Required Output :- 

# [[1,,1,1,1,1],
#  [1,,1,1,1,1],
#  [1,,1,1,1,1],
#  [1,,1,1,1,1],
#  [1,,1,1,1,1],
#  [1,,1,1,1,1],
#  [1,,1,1,1,1],]

# input :- 

import random


x = int(input(" Give X : "))
y = int(input(" Give Y : "))
arr = []
for row in range(x):
    temp_arr = []
    for col in range(y):
        temp_arr.append(random.randint(0,x**y))
    arr.append(temp_arr)


# print(arr)

# arr=[[ random.randint(0,x**y) for i in range(x)] for j in range(y)]
print(arr)