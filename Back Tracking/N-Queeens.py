def isvalidPos(board , curr , i):
    for k in range(curr):
        if curr-k == abs(i - board[k]) or i== board[k]:
            return False
        return True
        


def nqueen(size):
    board = [-1]*size
    curr = 0
    while curr!= -1:
        print(curr , board)
        placeFound = False
        for i in range(board[curr]+1 , size):
            placeFound = isvalidPos(board , curr , i)
            if placeFound:
                board[curr]=i
                curr+=1
                break
        if curr == size:
            print(board)
            board[-1] = -1
            curr = size-2 
        if not placeFound:
            board[curr] = -1
            curr-=1
    

nqueen(8)
    

