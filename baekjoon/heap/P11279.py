import heapq
import sys

N = int(input())

heap = []
for _ in range(N):
    X = int(sys.stdin.readline().strip())
    
    if X == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-X, X))
