def rotate(matrix):
    
        for row in matrix:
            row.reverse()
    
        n = len(matrix)
        for i in range(n):
            for j in range(n-i):
                matrix[i][j] , matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1] , matrix[i][j]  
        return matrix




print(rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))



