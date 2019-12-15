from heapq import heapify, heappush, nlargest
heap = [1,3]
heappush(heap, 2)
print(heap)
print(nlargest(2, heap))

