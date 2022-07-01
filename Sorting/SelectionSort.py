# sample array
#[10,20,3,5,6,77,3,73,7,7]

def SelectionSorting(array):
    size=len(arr)
    for s in range (size):
        min=s
        for i in range(s+1,size):
            if array[i]<array[min]:
                min=i
        array[s],array[min]=array[min],array[s]
    print(array)

# calling the function
arr=[10,20,3,5,6,77,3,73,7,7]
SelectionSorting(arr)
