                                                # Example 1:

# Input: 
# 2
# 0 4 
# 5
# Output: 
# 20
# Explanation: 
#     Increment the first number 5 times. Now nums = [5 4], with a product of 5 * 4 = 20. It can be shown that 20 is maximum product possible, so we return 20. Note that there may be other ways to increment nums to have the maximum product.

import heapq

def solve(n, nums, k):
    heapq.heapify(nums)
    for el in range(k):
        ans = nums[0]+1
        heapq.heappop(nums) 
        heapq.heappush(nums,ans)
    rr = 1  
    for i in nums:
        rr *= i

    return rr%(10**9+7) if rr>10**9+7 else rr        

TestCase =  [1,20,5,43,56,6,76,7,78,4,57,67]
print(solve(len(TestCase) , TestCase , 6))