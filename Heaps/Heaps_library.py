import heapq

hp = [2,3,5,100,1,6,19]
hp2 = hp[:]

#ALways Convert it to Minheap
heapq.heapify(hp)
print(hp)
#ALways Convert it to Maxheap
heapq._heapify_max(hp)
print(hp)