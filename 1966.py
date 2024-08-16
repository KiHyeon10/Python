from collections import deque

N = int(input())

for _ in range(N):
    total, target_index = map(int, input().split())
    queue = deque([(idx, priority) for idx, priority in enumerate(map(int, input().split()))])
    print_order = 0
    
    while queue:
        current = queue.popleft()
        
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            print_order += 1
            if current[0] == target_index:
                print(print_order)
                break
