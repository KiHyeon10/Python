import sys
import math
input = sys.stdin.readline

Ax, Ay, Bx, By, Cx, Cy = map(int, input().split())

if ((Ax-Bx)*(Ay-Cy)==(Ay-By)*(Ax-Cx)):
    print(-1.0)
else:
    AB = ((Ax-Bx)**2 + (Ay-By)**2)**0.5
    AC = ((Ax-Cx)**2 + (Ay-Cy)**2)**0.5
    BC = ((Bx-Cx)**2 + (By-Cy)**2)**0.5

    length = [AB+AC, AB+BC, AC+BC]
    answer = max(length) - min(length)
    print(2*answer)