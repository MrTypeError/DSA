def solve(n, arr, x, y):
    temp = 0
    sumOfNum = 0
    while x != y+1:
        sumOfNum += arr[x]
        x += 1
        temp += 1
    result=sumOfNum/temp
    return result 
