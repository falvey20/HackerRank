from collections import deque

N = int(input())
queue = deque()
for i in range(N):
    operation = input().split()
    op, val = operation[0], operation[1] if len(operation) == 2 else None
    if op == 'append':
        queue.append(val)
    elif op == 'appendleft':
        queue.appendleft(val)
    elif op == 'pop':
        queue.pop()
    elif op == 'popleft':
        queue.popleft()
print(' '.join(queue))
