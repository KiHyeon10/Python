import sys
input = sys.stdin.readline

T = int(input())

def Find_Location(Stack, col, row, Remove):
    if col < 0 or col > N-1 or row < 0 or row > M-1:
        return -1
    if Field[col][row] == 1 and Remove[Cabbage.index([col, row])] != False:
        Stack.append(Cabbage.index([col, row]))

for _ in range(T):
    M, N, K = map(int, input().split())
    Field = [[0 for i in range(M)] for j in range(N)]
    Cabbage = []
    Remove = [True] * K

    for _ in range(K):
        row, col = map(int, input().split())
        Field[col][row] = 1
        a = [col, row]
        Cabbage.append(a)
    i = 0
    count = 0
    Stack = []

    while True in Remove:
        col = Cabbage[i][0]
        row = Cabbage[i][1]
        Remove[Cabbage.index([col, row])] = False

        Find_Location(Stack, col-1, row, Remove)
        Find_Location(Stack, col, row-1, Remove)
        Find_Location(Stack, col+1, row, Remove)
        Find_Location(Stack, col, row+1, Remove)

        if True not in Remove:
            Stack.clear()
        
        if len(Stack) == 0:
            if True in Remove:
                i = Remove.index(True)

            count += 1
        else:
            i = Stack.pop()

    print(count)    
