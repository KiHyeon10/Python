import sys
input = sys.stdin.readline

T = int(input())
Word = []
count = T

for i in range(T):
    w = input().rstrip()
    Word.append(w)
Word.sort(reverse=True)

for i in range(T-1):
    if Word[i][:len(Word[i+1])] == Word[i+1]:
        count -= 1

print(count)