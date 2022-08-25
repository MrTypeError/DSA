
class Node:
    def __init__(self ,  data , left , right) -> None:
        self.data = data
        self.left = left
        self.right = right 
       
        def PostOrder(root):
            PostOrder(root.left)
            PostOrder(root.right)
            print(root.data)



a= Node("A", Node("B" , Node("D") , Node("E")), Node("C" , Node("F"),Node("G")))