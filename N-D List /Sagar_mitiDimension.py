temp_list , Ans = [] , []
Dim = int(input("Dimension : "))
def ThreeD_Mat(arr , x = 0 ,y = 0, z = 0 ):
    arr2=[]
    for row in range(x):
        temp_arr = []
        for col in range(y):
            temp_arr.append(1)
            temp_arr2=[]
            for high in range(z):
                temp_arr2.append(temp_arr)
            arr.append(temp_arr)
        arr2.append(arr)
    return(arr2)
    
while True:
    Choice = input("Enter The Choice : ")
    if Choice == "Y" or  Choice == "y" :
            for i in range(Dim):
                Dimension = int(input(f" Enter {chr(65+i)} : "))
                temp_list.append(Dimension)
    elif Choice == "N" or  Choice == "n" :
        break

NewArr = temp_list.reverse()
size = len(temp_list)
for i in range(size):
        x = temp_list.pop()
        y = temp_list.pop()
        z = temp_list.pop()
        Ans=ThreeD_Mat(temp_list,x,y,z)



# [[[1,1],[1,1],[1,1],[1,1],
# [[1,1],[1,1],[1,1],[1,1]],
# [[1,1],[1,1],[1,1],[1,1]],
# [[1,1],[1,1],[1,1],[1,1]]]]

# [[[1, 1],[1, 1],[1, 1]],
# [[1, 1],[1, 1],[1, 1]],
# [[1, 1],[1, 1],[1, 1]]]