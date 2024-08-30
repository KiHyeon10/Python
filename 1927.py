import sys
import heapq

input = sys.stdin.readline

T = int(input())

heap = []

for _ in range(T):
    com = int(input())
    
    if com == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, com)
