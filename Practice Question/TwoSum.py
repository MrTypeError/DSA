def twoSum(n, nums, target):
    # Time Complexity = O(n**2) 
    # Time Limit will exceed with certain cases
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target and i!=j:
                    return [min(i,j),max(i,j)]


#####################################################################
        # BOTH THE SOLUTIONS ARE CORRECT BUT 2ND IS MORE OPTIMIZED
#####################################################################

def twoSum(n,nums,target):
    m=dict()
    for index , element in enumerate(nums):
        if target - element in m:
            return[m[target - element] , index]
        m[element] = index


print(twoSum(6,[1,2,3,4,5,6,23],9))