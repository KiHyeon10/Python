<<<<<<< HEAD
import sys

input = sys.stdin.readline

a = input()

a = a.replace('XXXX', 'AAAA')
a = a.replace('XX', 'BB')

if 'X' in a:
    print(-1)
else:
=======
import sys

input = sys.stdin.readline

a = input()

a = a.replace('XXXX', 'AAAA')
a = a.replace('XX', 'BB')

if 'X' in a:
    print(-1)
else:
>>>>>>> 8bfc797ba1217368e52539de53646912d6b969c6
    print(a)