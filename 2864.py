import sys

input = sys.stdin.readline

A, B = list(input().split())

Max_A = []
Min_A = []
Max_B = []
Min_B = []

for i in range(len(A)):
    if A[i] == '6':
        Min_A.append('5')
        Max_A.append(A[i])
    elif A[i] == '5':
        Min_A.append(A[i])
        Max_A.append('6')
    else:
        Min_A.append(A[i])
        Max_A.append(A[i])

for i in range(len(B)):
    if B[i] == '6':
        Max_B.append(B[i])
        Min_B.append('5')
    elif B[i] == '5':
        Max_B.append('6')
        Min_B.append(B[i])
    else:
        Min_B.append(B[i])
        Max_B.append(B[i])

print(int(''.join(Min_A)) + int(''.join(Min_B)), end=' ')
print(int(''.join(Max_A)) + int(''.join(Max_B)))