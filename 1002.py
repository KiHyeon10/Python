import sys
import math

input = sys.stdin.readline

a = int(input())
point = []
for _ in range(a):
    point = list(map(int, input().split()))
    line = math.sqrt(abs((point[0] - point[3])**2) + abs((point[1] - point[4])**2))

    if line == 0 and point[2] == point[5]:
        print(-1)
    else:
        if point[2] + point[5] > line > abs(point[2] - point[5]):
            print(2)
        
        elif point[2] + point[5] == line or abs(point[2] - point[5]) == line:
            print(1)
        
        else:
            print(0)