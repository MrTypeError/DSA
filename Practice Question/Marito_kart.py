'''Input:
    7 2
    1 41
    3 47
    6 41
    4 50
    7 36
    2 47
    5 50
Output:
    1 6
Explanation:
    7 2 is the size of the leaderboard. The second lowest score is 41 and the corresponding players are 1 and 6.

####################################################################################################################################################################################

Input:
    5 2
    3 37
    1 41
    2 37
    5 41
    4 35
Output:
    2 3
Explanation:
     5 2 is the size of the leaderboard. The second lowest score is 37 and their corresponding players are 2 and 3.
'''


def solve(mat):
    fm = float("inf")
    sm = float("inf")
    ans = []
    for e in mat:
        if e[1]<fm:
            sm=fm
            fm=e[1]
        elif fm<e[1]<sm:
            sm=e[1]
    
    for e in mat:
        if e[1]==sm:
            ans.append(e[0])
    return sorted(ans)


mat=[
    [5,2],
    [3,37],
    [1,41],
    [2,37],
    [5,41],
    [4,35]
]

newVar=solve(mat)
print(newVar)

# newDict={}

# for row in mat:
#     newDict[row[0]]=row[1]
    # newDict.update({row[0]:row[1]})
    
# for key,value in newDict.items():



# for row in mat:
#     for col in row:
#         m.update({col[0]:col[1]})




# for i in mat:
#     print(i[0])
#     print(i[1])
#     print("---")

