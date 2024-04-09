import heapq

heap=[5,9,8,3]
heapq.heapify(heap)
heapq.heappop(heap)
heapq.heappush(heap,6)
heapq.heappush(heap,9)
node=heapq.heappop(heap)
minNode=heapq.heappop(heap)
print(minNode)

maxNode=heapq.heappop(heap)
print(maxNode)
print(heap)