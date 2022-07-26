class Node:

    def __init__(self ,  data , left , right) -> None:
        self.data = data
        self.left = left
        self.right = right 


        def inOrder(root):
            if root:
                inOrder(root.left)
                print(root.data)
                inOrder(root.right)


a= Node("A", Node("B" , Node("D") , Node("E")), Node("C" , Node("F"),Node("G")))