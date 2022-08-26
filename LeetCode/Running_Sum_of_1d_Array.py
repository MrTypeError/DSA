# 1480. Running Sum of 1d Array
# 1480. Running Sum of 1d Array




def runningSum(nums):
    previous  = 0
    curr = 1
    n= len(nums)
    for i in range(n):
        if i<n-1:
            nums[curr]+= nums[previous]
            previous+=1
            curr+=1
    return nums 
        

print(runningSum([1,2,3,4]))
