class Node:
    def __init__(self , data , left , right) -> None:
        self.data= data
        self.left = left
        self.right = right
        
def f(root , sum):
    if root :
        ans = (2*sum)+root.val
        if not root.left and not root.right:
            return ans
        return f(root.left , ans)+f(root.right , ans)
    return 0


def solve(root):
    return f(root,0)

