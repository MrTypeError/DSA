# Input:

#     3 3  NXN 2D Matrix

#     1 2 3
#     4 5 6
#     7 8 9

# Output:

#     7 4 1
#     8 5 2
#     9 6 3



def solve(mat):
    for row in mat:
        row.reverse()
    n = len(mat)
    for i in range(n):
        for j in range(n-i):
            mat[i][j] , mat[n-j-1][n-i-1] = mat[n-j-1][n-i-1] , mat[i][j]  
    return mat
