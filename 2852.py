import sys

input = sys.stdin.readline

N = int(input())
Team = []
Shoot = []

for _ in range(N):
    T, S = input().split()
    Team.append(int(T))
    Shoot.append(S.split(':'))

A = 0
A_flag = 0
Before_Start = [0, 0]
Start = [0, 0]
A_count = [0, 0]
B_count = [0, 0]

for i in range(N):
    if Team[i] == 1:
        A += 1
        A_flag = 1
    elif Team[i] == 2:
        A -= 1
        A_flag = 2
    
    if A == 0:
        Before_Start = Start.copy()
        Start = [int(Shoot[i][0]), int(Shoot[i][1])]
        if Start[1] < Before_Start[1]:
            Start[0] -= 1
            Start[1] += 60
        if A_flag == 1:
            B_count[0] += Start[0] - Before_Start[0] + ((Start[1] - Before_Start[1]) // 60)
            B_count[1] += (Start[1] - Before_Start[1]) % 60
        elif A_flag == 2:
            A_count[0] += Start[0] - Before_Start[0] + ((Start[1] - Before_Start[1]) // 60)
            A_count[1] += (Start[1] - Before_Start[1]) % 60
        A_flag = 0

    if A == 1 and A_flag == 1:
        Start = [int(Shoot[i][0]), int(Shoot[i][1])]
    elif A == -1 and A_flag == 2:
        Start = [int(Shoot[i][0]), int(Shoot[i][1])]

End = [48, 0]

if A > 0:
    if Start[1] > 0:
        End[0] -= 1
        End[1] += 60
    A_count[0] += End[0] - Start[0] + ((End[1] - Start[1]) // 60)
    A_count[1] += (End[1] - Start[1]) % 60
elif A < 0:
    if Start[1] > 0:
        End[0] -= 1
        End[1] += 60
    B_count[0] += End[0] - Start[0] + ((End[1] - Start[1]) // 60)
    B_count[1] += (End[1] - Start[1]) % 60

if A_count[1] >= 60:
    A_count[0] += A_count[1] // 60
    A_count[1] = A_count[1] % 60
if B_count[1] >= 60:
    B_count[0] += B_count[1] // 60
    B_count[1] = B_count[1] % 60

if A_count[0] < 10 and A_count[1] > 1:
    print(0, end='')
    print(A_count[0],end=':')
elif A_count[0] == 0:
    print('00',end=':')
else:
    print(A_count[0],end=':')

if A_count[1] < 10 and A_count[1] > 1:
    print(0,end='')
    print(A_count[1])
elif A_count[1] == 0:
    print('00')
else:
    print(A_count[1])

if B_count[0] < 10 and B_count[1] > 1:
    print(0, end='')
    print(B_count[0],end=':')
elif B_count[0] == 0:
    print('00',end=':')
else:
    print(B_count[0],end=':')

if B_count[1] < 10 and B_count[1] > 1:
    print(0,end='')
    print(B_count[1])
elif B_count[1] == 0:
    print('00')
else:
    print(B_count[1])