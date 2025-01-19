import sys
input = sys.stdin.readline

N = int(input())

words = {input().strip() for _ in range(N)}

answer = sorted(words, key=lambda x: (len(x), x))

print('\n'.join(answer))
