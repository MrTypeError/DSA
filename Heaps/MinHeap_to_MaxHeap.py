import heapq
hp  =[2,3,4,1,14,5,51,100,13,4,32]

# Using built-in function
# -----------------------------


# heapq.heapify(hp)
# print(hp)

# heapq._heapify_max(hp)
# print(hp)


hp = [-x for x in hp]
heapq.heapify(hp)
hp = [-x for x in hp]
print(hp)
 
