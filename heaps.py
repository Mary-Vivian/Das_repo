import heapq

heap=[5,9,8,3]
heapq.heapify(heap)
print(heap)

heapq.heappop(heap)
print(heap)

heapq.heappush(heap,6)
print(heap)
heapq.heappushpop(heap,9)
print(heap)

heapq.heapreplace(heap,4)
print(heap)
heap.sort()
print(heap)
