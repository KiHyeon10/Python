import sys

input = sys.stdin.readline

def Find(array):
    count = []
    Max = array.count(array[0])
    count.append(array[0])
    
    for i in range(1, len(array)):
        if array[i-1] != array[i]:
            counting = array.count(array[i])
            if Max == counting:
                count.append(array[i])
            elif Max < counting:
                count.clear()
                Max = counting
                count.append(array[i])

    if len(count) != 1:
        return count[1]
    else:
        return count[0]

N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

num.sort()

print(round(sum(num)/N))

if N-1 != 0:
    print(num[(N-1)//2])
else:
    print(num[0])

array = num.copy()
answer = Find(array)

print(answer)

if N != 1:
    print(round(num[N-1] - num[0]))
else:
    print(0)
