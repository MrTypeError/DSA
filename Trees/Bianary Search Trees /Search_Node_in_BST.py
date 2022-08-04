import sys
sys.setrecursionlimit(10**6)
def SearchBianarySearchTree(root, target):
    if root is None :
        return dummyNode
    if root.val == target:
        return root 
    if root.val > target:
        return SearchBianarySearchTree(root.left, target)
    else:
        return SearchBianarySearchTree(root.right, target)

dummyNode = TreeNode(-1)
def solve(root, target):
    return SearchBianarySearchTree(root, target)

