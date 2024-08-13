import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
answer = []

for _ in range(N):
    num = int(input())
    
    if num == 0:
        if len(heap) == 0:
            answer.append(0)
        else:

            answer.append(heapq.heappop(heap)[1])
    else:

        heapq.heappush(heap, (abs(num), num))


print(*answer, sep='\n')
