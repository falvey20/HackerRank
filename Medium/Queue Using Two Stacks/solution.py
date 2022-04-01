from collections import deque
q = int(input())
queue = deque()

for i in range(q):
    item = input()
    if item[0] == '1':
        op, num = int(item.split()[0]), int(item.split()[1])
        queue.append(num)
    elif item == '2':
        queue.popleft()
    elif item == '3':
        print(queue[0])
