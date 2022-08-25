def mark_the_current_island(matrix,x,y,r,c):
    
        if x<0 or x>=r or y<0 or y>=c or matrix[x][y]!='1': #Boundary Conditions 
            return    

        matrix[x][y] = '2'

        mark_the_current_island(matrix ,x+1, y , r,c) #DOWN
        mark_the_current_island(matrix ,x, y+1 ,r,c) #RIGHT
        mark_the_current_island(matrix ,x-1, y , r,c) #TOP
        mark_the_current_island(matrix ,x, y-1 , r,c) #LEFT

def solve(grid):
        rows = len(grid)
        if rows == 0:
            return 0
        col = len(grid[0])

        countofislands = 0
        
        for i in range(rows):
            for j in range(col):
                if grid[i][j]== '1':
                    mark_the_current_island(grid,i,j,rows,col)
                    countofislands+=1
        return countofislands



print(solve(solve(grid = [
                            ["1","1","1","1","0"],
                            ["1","1","0","1","0"],
                            ["1","1","0","0","0"],
                            ["0","0","0","0","0"]
                        ])))
