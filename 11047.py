import sys
input = sys.stdin.readline

a, b = map(int, input().split())
money = []
count = 0

while a != 0:
    money.insert(0, int(input()))
    a -= 1
 
for j in money:
   count += b//j
   b %= j
   
print(count)

