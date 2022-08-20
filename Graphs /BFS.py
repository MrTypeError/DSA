# -----------------------------------------------------------
                            # BFS
# -----------------------------------------------------------

from collections import deque


def BFS(adj):
    print("BFS")
    vis = set()
    n = len(adj)
    for i in range(n):
        if i in vis :
            continue
        vis.add(i)
        q = deque([i])
        while q:
            el = q.pop()
            print(el , end="")
            for adjel in range(n):
                if [el][adjel] and adjel not in vis:
                    vis.add(adjel)
                    q.appendleft(adjel)
    print()

