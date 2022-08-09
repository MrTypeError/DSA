class Node:
    def __init__(self ,  data , left= None , right =None) -> None:
        self.data = data
        self.left = left
        self.right = right

NewSet = set()
def solve(root, k):
    if root == None :
        return 0
    if (k-(root.data)) in NewSet :
        return 1
    NewSet.add(root.data)
    return solve(root.left , k) or solve(root.right ,k)

root = Node(11,
            Node(7,Node(14),Node(3)),
            Node(9, Node(12))
            )
# print(solve(root,9))