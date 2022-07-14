def solve(board):
    ans = 0
    rows , cols = len(board), len(board[0])
    for i in range (rows):
        for j in range(cols):
            if board[i][j] == "X" and (i==0 or board[i-1][j] !="X" ) and (j== 0 or board[i][j-1]!="X"):
                ans+=1
    return ans

