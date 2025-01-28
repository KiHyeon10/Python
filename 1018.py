import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

# 체스판의 두 가지 패턴
Board1 = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

Board2 = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]

def Find(x, y):
    Counting1 = 0
    Counting2= 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != Board1[i][j]:
                Counting1 += 1
            if board[x + i][y + j] != Board2[i][j]:
                Counting2 += 1
    return min(Counting1, Counting2)

count = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        count = min(count, Find(i, j))

print(count)
