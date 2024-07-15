import sys

input = sys.stdin.readline

n, w, L = map(int, input().split())

Truck = list(map(int, input().split()))

Bridge = [0] * w
count = 0

while len(Bridge) != 0:
    Bridge = Bridge[1:]
    if len(Truck) != 0:
        if sum(Bridge) + Truck[0] <= L:
            Bridge.append(Truck.pop(0))
        else:
            Bridge.append(0)
    
    count += 1

    
print(count)