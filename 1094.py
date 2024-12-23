import sys
input = sys.stdin.readline

X = int(input())

Stick = [64]

while sum(Stick) != X:
    a = min(Stick) / 2
    Stick.remove(min(Stick))

    if (a + sum(Stick)) >= X:
        Stick.append(a)
    else:
        Stick.append(a)
        Stick.append(a)


print(len(Stick))