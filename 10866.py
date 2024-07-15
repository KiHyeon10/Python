import sys

input = sys.stdin.readline

N = int(input())
Deque = []
answer = []

for i in range (0, N):
    Com= input().split()
    
    if Com[0] == "push_front":
        Deque.insert(0, int(Com[1]))
        
    elif Com[0] == "push_back":
        Deque.insert(len(Deque), int(Com[1]))
        
    elif Com[0] == "pop_front":
        if len(Deque) == 0:
            answer.append(-1)
        else:
           answer.append(Deque.pop(0))
    
    elif Com[0] == "pop_back":
        if len(Deque) == 0:
            answer.append(-1)
        else:
            answer.append(Deque.pop(len(Deque) - 1))
    
    elif Com[0] == "size":
        answer.append(len(Deque))
    
    elif Com[0] == "empty":
        if len(Deque) == 0:
            answer.append(1)
        else:
            answer.append(0)
    
    elif Com[0] == "front":
        if len(Deque) != 0:
            answer.append(Deque[0])
        else:
            answer.append(-1)
    elif Com[0] == "back":
        if len(Deque) != 0:
            answer.append(Deque[len(Deque) - 1])
        else:
            answer.append(-1)

for i in range(0, len(answer)):
    print(answer[i])