import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

def Find(A, B):
    length_A, length_B = len(A), len(B)
    Min = length_A + length_B

    for i in range(-length_B + 1, length_A):
        flag = True
        for j in range(length_B):
            pos_A = i + j
            if 0 <= pos_A < length_A and A[pos_A] == '2' and B[j] == '2':
                flag = False
                break
        if flag:
            Min = min(Min, max(length_A, i + length_B) - min(0, i))

    return Min
print(Find(A, B))