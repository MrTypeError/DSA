# print(6,[1,2,3,4,5,4,7])

def solve(n, arr):
    l2=list()
    for i in range(len(arr)):
        if arr[i] not in l2:
            l2.append(arr[i])

    if len(l2) == len(arr):
        print("0")
    else:
        print("1")

    
    # print("1") if  len(l2) != n else print("0")
        



solve(6,[1,2,3,4,5,4,7])