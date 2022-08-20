'''
    Creating a input for the
    directed graph using 
    adjecency Matrix 
'''

def adjecency_matrix_directed(edges):
    NumOfNode = 1+ max([e[1]for e in edges] + [e[0]for e in edges] )
    adj = [[0]*NumOfNode  for i in range(NumOfNode)]
    for e in edges:
        adj[e[0]][e[1]] = 1
    return adj

directed_edges = adjecency_matrix_directed([[0,1],
                                                [1,2],
                                                [1,3],
                                                [2,4],
                                                [3,4],
                                                [5,7],
                                                [7,6]]) 
print(directed_edges)