a = int(input())
C= []
coin = [25, 10, 5, 1]
for i in range(0, a):
    C.append(int(input()))

for j in C:
    for s in coin:
        print(j//s, end = ' ')
        j %= s
    print(end = '\n')
    