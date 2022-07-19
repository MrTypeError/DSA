def solve(grid):
    rottern_q= deque()
    m,n= len(grid), len(grid[0])
    fresh_oranges = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                fresh_oranges+=1
            elif grid[i][j]==2:
                rottern_q.appendleft((i,j,0))

    if not fresh_oranges:
        return 0
        #This will be heping in checking the elements 
    directions ={
        (1,0),
        (-1,0),
        (0,1),
        (0,-1)
    }
    while rottern_q:
        ro_i,ro_j,time=rottern_q.pop()
        for di , dj in directions:
            newo_i, newo_j=ro_i+di, ro_j+dj
            fresh_oranges-=1
            if  not fresh_oranges:
                return time+1
            grid[newo_i][newo_j]=2
            rottern_q.appendleft((newo_i,newo_j,time+1))
    return -1
