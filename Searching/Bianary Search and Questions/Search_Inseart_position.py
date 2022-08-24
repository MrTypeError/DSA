def solve(n, nums, target):
    left = 0
    right = len(nums) -1
    
    while left <= right:
        mid = (right + left) // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid]  < target:
            left = mid+1
        
        elif nums[mid] > target:
            right = mid-1
        
    return left

# ---------------------------
            # OR
# ---------------------------


def solve(n,nums,target):
    if target in nums:
    
    #output the index position of 'target' 
        return nums.index(target)

    #if target doesn't exist in 'nums' list then add it to the list
    else:
    
        #add target to 'nums'
        nums.append(target)
        
        #sort 'nums' list by ascending order
        sortednums = sorted(nums)
        
        #return the index position of target in 'sortednums'
        return sortednums.index(target)


print(solve(5,[1,3,4,5,10],2))
