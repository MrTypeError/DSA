import heapq
def solve(matrix, k):
    hp = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            heapq.heappush(hp, matrix[i][j])
    
    for i in range(1,k):
        heapq.heappop(hp)
    
    return hp[0]




print(solve([[3,3],
            [1,5,9],
            [10,11,13],
            [12,13,15]] , 8))