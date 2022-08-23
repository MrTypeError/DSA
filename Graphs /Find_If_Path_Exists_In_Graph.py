from collections import defaultdict

def solve(n, edges, source, destination):

    # '''
    #     Not Efficient but has a correct Logic 
    # '''
    # if n==1 or [source , destination] in edges:
    #     return 1

    
    # m = defaultdict(list)
    # for k, v in edges:
    #     m[k].append(v)


    # def dfs(m , src , dsty , vis):
    #     if src == dsty:
    #         return 1
    #     if src in vis:
    #         return 0
    #     vis.add(src)
    #     for key in m[src]:
    #         if dfs(m , key , dsty ,vis):
    #             return 1
    # return dfs(m , source ,destination , set())

    # '''
    #     Not Efficient but has a correct Logic 
    # '''

        # def validPath(self, n, edges, source, destination):
        #     adj=defaultdict(list)
        # for e in edges:
        #     adj[e[0]].append(e[1])
        #     adj[e[1]].append(e[0])
    
        # def dfs(s):
        #     visited.add(s)
            
        #     for node in adj[s]:
        #         if node not in visited:
        #             dfs(node)
        
        # visited=set()
        # dfs(source)
        # if destination in visited:
        #     return True
        # return False

        adjacency=[[] for i in range(n)]
        
        for i in range(len(edges)):
            adjacency[edges[i][0]].append(edges[i][1])
            adjacency[edges[i][1]].append(edges[i][0])
            
        queue=[source]
        
        seen_set=set()
        
        while len(queue)>0:
            node=queue.pop(0)
            
            if node==destination:
                return 1
            
            if node not in seen_set:
                seen_set.add(node)
                for i in range(len(adjacency[node])):
                    queue.append(adjacency[node][i])
        
        return 0




print(solve(10,[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]],7,5))