class Node:
    def __init__(self ,  data , left , right) -> None:
        self.data = data
        self.left = left
        self.right = right 
       
        def PreOrder(root):
            print(root.data)
            PreOrder(root.left)
            PreOrder(root.right)



a= Node("A", Node("B" , Node("D") , Node("E")), Node("C" , Node("F"),Node("G")))