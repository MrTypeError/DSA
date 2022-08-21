'''
    Don't use BFS to detect the cycle in Directed Graph.
    It will be very complex and the program will not be
    efficient 
'''


def DFS_recursive_path(adj , vis , path , el):
    vis.add(el)
    path.add(el)
    for adj_el in range(len(adj)):
        if adj[el][adj_el]:
            if adj_el not in vis:
                if DFS_recursive_path(adj , vis , path , adj_el):
                    return True 
            elif adj_el in path :
                print(f"Cycle Found {el} - {adj_el} ")
                return True
    path.remove(el)
    return False



def detect_cycle_directed(adj):
    vis = set()
    path = set()
    n = len(adj)
    for i in range(n):
        if i in vis :
            continue
        if DFS_recursive_path(adj , vis ,path , i ):
            return 
    print("No Cycles Found")



adj =[[0, 1, 0, 0, 0, 0, 0, 0], 
      [1, 0, 1, 1, 0, 0, 0, 0],
      [0, 1, 0, 0, 1, 0, 0, 0],
      [0, 1, 0, 0, 1, 0, 0, 0],
      [0, 0, 1, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 1], 
      [0, 0, 0, 0, 0, 1, 1, 0]]

detect_cycle_directed(adj)