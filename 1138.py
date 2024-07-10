import sys

input = sys.stdin.readline

N = int(input())
Person = list(map(int, input().split()))
Line = [0] * N

Where_is_empty = [index for index, element in enumerate(Line) if element == 0]

for i in range (0, N):
    #Line중 아직 줄 서지 않은 곳을 알려줌
    if Person[i] == 0:
        Line[Where_is_empty[0]] = i + 1
        del(Where_is_empty[0])
    else:
        Line[Where_is_empty[Person[i]]] = i + 1
        del(Where_is_empty[Person[i]])

print(Line)