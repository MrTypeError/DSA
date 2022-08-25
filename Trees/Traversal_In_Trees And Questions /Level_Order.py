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

###################################################################################################
                                            # OR
###################################################################################################


def solve(root):
    q = [root] 
    ans = []

    while len(q) > 0 :
        lvl_vals = []
        for i in range(len(q)):
            curr = q[0]
            q = q[1:]
            lvl_vals.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        ans.append(lvl_vals)
    return ans


###################################################################################################
                                        # FUNCTION CALL
###################################################################################################

a= Node("A", Node("B" , Node("D") , Node("E")), Node("C" , Node("F"),Node("G")))
print(level_order(a , []))