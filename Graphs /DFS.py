from collections import deque


def DFS(adj):
    print("DFS")
    vis = set()
    n = len(adj)
    for i in range(n):
        if i in vis:
            continue
        vis.add([i])
        st = deque([i])
        while st:
            el = st.pop()
            print(el , end="")
            for adjel in range(n):
                if adj[el][adjel] and adjel not in vis :
                    vis.add(adjel)
                    st.append(adjel)