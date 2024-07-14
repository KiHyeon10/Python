import sys

input = sys.stdin.readline

i = input().strip()

room = []
answer = [0] * 10

room = [int(num) for num in i]

for a in range (0, len(room)):
    answer[room[a]] += 1

print(answer)
if answer.index(max(answer)) == 6 or answer.index(max(answer)) == 9:
    sum = answer[6] + answer[9]
    if sum % 2 == 0:
        answer[6] = int(sum / 2)
        answer[9] = int(sum / 2)
    else:
        answer[6] = int(sum / 2) + 1
        answer[9] = int(sum / 2) + 1

print(max(answer))