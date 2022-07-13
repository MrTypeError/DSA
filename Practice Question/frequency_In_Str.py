def solve(str1):
    arr=[]
    arr2=[]
    for i in str1:
        if i not in arr2 :
            arr.append(str1.count(i))
            arr2.append(i)
    return arr


print(solve("arfardarb"))
