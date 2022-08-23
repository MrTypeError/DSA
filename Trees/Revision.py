class Node:
    def __init__(self , data , left=None , right=None):
        self.data = data
        self.right = right 
        self.left = left 



def post_order(n):
    if  not n:
        return
    post_order(n.left)
    post_order(n.right)
    print(n.data)

 





root = Node(1,Node(2, Node(6)),Node(3,Node(4, None ,Node(7)),Node(5)))

print(post_order(root))