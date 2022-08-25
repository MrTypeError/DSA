class Node:
    def __init__(self ,  data , left=None , right=None) -> None:
        self.data = data
        self.left = left
        self.right = right 

def f(root,k,isleft):
    if root:
        if isleft:
            return max(f(root.left ,1 ,True), f(root.right , k+1, False))
        else:
            return max(f(root.left , k+1, True) ,f(root.right ,1 ,False))
    return k-1

def solve(root):
    return f(root , 0 ,True)
    