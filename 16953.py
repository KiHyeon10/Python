<<<<<<< HEAD
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

count = 1

while b != a:
    temp = b
    if b%10 == 1:
        b = b//10
        count += 1
    
    elif b%2 == 0:
        b = b//2
        count += 1
        
    if temp == b:
        print(-1)
        break

if b == a:
=======
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

count = 1

while b != a:
    temp = b
    if b%10 == 1:
        b = b//10
        count += 1
    
    elif b%2 == 0:
        b = b//2
        count += 1
        
    if temp == b:
        print(-1)
        break

if b == a:
>>>>>>> 8bfc797ba1217368e52539de53646912d6b969c6
    print(count)