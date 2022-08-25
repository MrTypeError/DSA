# This is the level order approach 
#to find the maximum depth of the Bianary Tree 
################################################################
                        # BFS
################################################################
def solve_BFS(root):
    if not root:
        return 0
    depth = 0
    q = []
    q.append(root)
    while q:
        depth+=1
        temp = []
        for node in q:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        q = temp
    return depth



# This is the DFS approach 
#to find the maximum depth of the Bianary Tree 

################################################################
                        # DFS
################################################################
def solve_DFS(root):
    if not root:
        return 0
    left_sub_tree = solve_DFS(root.left)
    right_sub_tree = solve_DFS(root.right)

    return 1+max(left_sub_tree , right_sub_tree)




print(solve_BFS([3,9,20,None,None,15,7]))
print("------------------------------------")
print(solve_DFS([3,9,20,None,None,15,7]))
