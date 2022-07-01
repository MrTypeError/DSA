def InsertionSort(arr):
    n=len(arr)
    for wall in range(1,n):
        current=arr[wall]
        pos_ptr=wall-1
        while pos_ptr>=0 and current<arr[pos_ptr]:
            arr[pos_ptr+1]=arr[pos_ptr]
            pos_ptr-=1
        arr[pos_ptr+1]=current
    return arr

arr=[12,14,18,6,7,5,42,1]
InsertionSort(arr)
print(arr)