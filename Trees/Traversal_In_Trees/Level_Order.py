from collections import deque
class Node:
    def __init__(self , data , left =None , right =None) -> None:
        self.data= data
        self.left = left
        self.right = right


def level_order(root ,arr):
    # add element to start the queue and then start the loop
    q=deque([root])
    while q:
        #pop One element and print the element and then add left or right which exists
        temp = q.pop() 
        arr.append([temp.data])
        #It will append the element in the queue (the left elements)
        if temp.left:
            q.appendleft(temp.left)
        #It will append the element in the queue (the right elements) 
        if temp.right:
            q.appendleft(temp.right)
    return arr
a= Node("A", Node("B" , Node("D") , Node("E")), Node("C" , Node("F"),Node("G")))
print(level_order(a , []))