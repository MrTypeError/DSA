# # T.C :- O(nlogn)

import heapq
hp  =[2,3,4,1,14,233.5,51,100,13,4,32]
k=4
temp = len(hp)-k
hp2 = sorted(hp)
for index in range(len(hp2)):
    print(hp2[index])
    if index == temp-1:
        print(hp2[index])


# --------------------------------------------
                # MORE OPTIMIZED
# --------------------------------------------


# # T.C :- O(nlogk)
import heapq
def solve(n, nums, k):
    hp = []
    for el in nums :
        if len(hp)<k:
            heapq.heappush(hp , el)
        else:
            if hp[0] < el:
                heapq.heappush(hp , el)
                heapq.heappop(hp)
    return hp[0]
            

print(solve(6,[ 3, 2, 1, 5, 6, 4],2))
print(solve(6,[2,3,4,1,14,235,51,100,13,4,32],2))


