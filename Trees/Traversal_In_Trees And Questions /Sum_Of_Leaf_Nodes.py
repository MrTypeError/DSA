class Node:
    def __init__(self ,  data , left= None , right =None) -> None:
        self.data = data
        self.left = left
        self.right = right

def sum_of_leaf_node(root):
    if root:
        if root.left or root.right:
            return sum_of_leaf_node(root.left)+sum_of_leaf_node(root.right)
        return root.data
    return 0

root = Node(2,
            Node(3,Node(5),Node(6)),
            Node(4, Node(7))
            )
print(sum_of_leaf_node(root))
