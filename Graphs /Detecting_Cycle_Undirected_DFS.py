from collections import deque


def Detect_Cycle_Undirected_BFS(adj):
    vis = set()
    n = len(adj)
    for i in range(n):
        if i in vis :
            continue
        vis.add(i)
        q = deque([[i , -1]])
        while q :
            el , parent = q.pop()
            for adj_el in range(n):
                if adj[el][adj_el]:
                    if adj_el not in vis:
                        vis.add(adj_el)
                        q.append([adj_el , el])
                    elif adj_el != parent:
                        print(f"Cycle Fouund :  {el} - {adj_el}")
                        return
    print(" Cycle Not Found ")



adj =[[0, 1, 0, 0, 0, 0, 0, 0], 
      [1, 0, 1, 1, 0, 0, 0, 0],
      [0, 1, 0, 0, 1, 0, 0, 0],
      [0, 1, 0, 0, 1, 0, 0, 0],
      [0, 0, 1, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 1], 
      [0, 0, 0, 0, 0, 1, 1, 0]]

Detect_Cycle_Undirected_BFS(adj)