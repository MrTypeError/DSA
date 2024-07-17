# def InsertionSort(arr):
#     n=len(arr)
#     for wall in range(1,n):
#         current=arr[wall]
#         pos_ptr=wall-1
#         while pos_ptr>=0 and current<arr[pos_ptr]:
#             arr[pos_ptr+1]=arr[pos_ptr]
#             pos_ptr-=1
#         arr[pos_ptr+1]=current
#     return arr

# arr=[12,14,18,6,7,5,42,1]
# InsertionSort(arr)
# print(arr)


def insertionSort(arr):
    for i in range (1 , len(arr)):
        j=i
        while j > 0 and arr[j - 1] > arr[j]:
            arr [j - 1] ,  arr[j] = arr[j] , arr[j - 1]
            j-=1
    return arr
arr = [2, 3, 8, 1, 5 ]
print(insertionSort(arr))
