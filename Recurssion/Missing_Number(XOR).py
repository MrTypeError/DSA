def solve(n, arr):
    #non Optimized
    # n = len(arr)
    # return (n*(n+1))//2-sum(arr)

    #Optimization Using XOR : -
    # ans = 0
    # for i in arr:
    #     ans = ans^i
    # # for j in range(0, n-1):
    # for j in range(0,len(arr)-1):
    #     ans = ans^arr[i]
    # if len(arr) == 1:
    #     return ans-1
    # else:
    #     return ans
    ans = n
    for i in range(n):
        ans = ans ^ i ^ arr[i]
    return ans

# print(solve(5,[0,1,2,4,5]))
# print(solve(3,[3,0,1]))
# print(solve(1,[1]))

print(solve(9,[9,6,4,2,3,5,7,0,1]))

