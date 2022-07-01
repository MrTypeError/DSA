def bubble(arr):
    n=len(arr)
    for itr in range(n):
        for current in range(n-1-itr):
            if arr[current]>arr[current+1]:
                arr[current],arr[current+1]=arr[current+1],arr[current]
    return arr


arr=[10,20,3,5,6,77,3,73,7,7]
print(bubble(arr))
