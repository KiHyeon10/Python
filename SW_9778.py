TC = int(input())

for t in range(TC):
    N = int(input())
    card = []
    for _ in range(N):
        card.append(int(input()))
    extra = [4] * 12
    extra[10] = 16

    for i in range(N):
        extra[card[i]] -= 1

    total = sum(card)
    Target = 21 - total
    low = sum(extra[Target:1:-1])
    High = sum(extra[Target:])
    answer = "STOP" if High > low else "GAZUA"

    print(answer)