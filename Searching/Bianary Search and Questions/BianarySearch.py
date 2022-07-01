def Bianary(arr,x):
    low,high=0,len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if x==arr[mid]:
            return mid
        if x <arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1

            
arr=[1,2,3,4,5,67,72,89,90,100,119]
ans=Bianary(arr,72)
print(ans)
            
            