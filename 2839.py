<<<<<<< HEAD
import sys

input = sys.stdin.readline

n = int(input())
count = 0

while n%5 != 0:
    n -= 3
    count += 1
    if n < -1:
        print(-1)
        break;
    else:
        continue;
if n%5 == 0:
    count += n//5
=======
import sys

input = sys.stdin.readline

n = int(input())
count = 0

while n%5 != 0:
    n -= 3
    count += 1
    if n < -1:
        print(-1)
        break;
    else:
        continue;
if n%5 == 0:
    count += n//5
>>>>>>> 8bfc797ba1217368e52539de53646912d6b969c6
    print(count)