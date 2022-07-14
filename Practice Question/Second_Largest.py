def solve(n, arr):
    maximim=arr[0]
    arr.sort()
    for i in arr:
        temp=i-1
        if i>maximim:
            maximim=i

    return temp


print(solve(6,[2,1,2,8,7,8,997]))