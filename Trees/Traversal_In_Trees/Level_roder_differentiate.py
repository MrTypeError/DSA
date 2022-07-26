
from collections import deque
class Node:
    def __init__(self ,  data , left=None , right=None) -> None:
        self.data = data
        self.left = left
        self.right = right 
    
def level_order_differentiate(root):
    q= deque([None , root])
    while True:
        n = q.pop()
        if n:
            print(n.data)
            if n.left:
                q.appendleft(n.left)
            if n.right:
                q.appendleft(n.right)
        else:
            print("--------------")
            if q:
                q.appendleft(None)
            else:
                break
                


a= Node("A", Node("B" , Node("D") , Node("E")), Node("C" , Node("F"),Node("G")))

print(level_order_differentiate(a))

# Op

# A
# --------------
# B
# C
# --------------
# D
# E
# F
# G
# --------------
# None