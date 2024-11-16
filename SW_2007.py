T = int(input())

for t in range(T):
    S = input()
    Sen = [x for x in S]
    answer = []
    answer.append(Sen[0])

    for i in range(1, len(Sen)):
        if answer[0] != Sen[i]:
            answer.append(Sen[i])

        elif answer[0] == Sen[i]:
            if answer[-1] == Sen[i-1] and answer[1] == Sen[i+1]:
                break
            else:
                answer.append(Sen[i])

    print("#{0} {1}".format(t+1, len(answer)))