class Node:
    def __init__(self ,  data , left= None , right =None) -> None:
        self.data = data
        self.left = left
        self.right = right

def print_leaf_Nodes(root):
    if root:
        if not root.left and not root.right:
            print(root.data)
        else:
            print_leaf_Nodes(root.left)
            print_leaf_Nodes(root.right)
        
root = Node(2,
            Node(3,Node(5),Node(6)),
            Node(4, Node(7))
            )
print(print_leaf_Nodes(root))
