import sys

input = sys.stdin.readline

after, night, Day = map(int,input().split())

if (Day - night) % (after - night) == 0:
    print((Day-night) // (after-night))
else:
    print((Day-night) // (after-night) + 1)