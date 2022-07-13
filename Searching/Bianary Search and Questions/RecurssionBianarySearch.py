from traceback import print_tb


def solve(n, arr, x, y):
    SumOfNum = arr[x]
    Temp=0
    while x!=y:
        SumOfNum+= arr[x+1]
        x+=1
        Temp+=1
    result=SumOfNum/Temp
    return round(result, 2)


print( solve(6,[6,2 ,5 ,4 ,3 ,1],2,5))