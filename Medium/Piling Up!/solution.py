from collections import deque

T = int(input())
for i in range(T):
    n = int(input())
    cubes = deque([int(cube) for cube in input().split(' ')])
    last = max(cubes)
    result = True
    while cubes:
        if max(cubes[0], cubes[-1]) > last:
            result = False
            break
        else:
            if cubes[0] > cubes[-1]:
                last = cubes[0]
                cubes.popleft()
            else:
                last = cubes[-1]
                cubes.pop()
    if result == True:
        print('Yes')
    else:
        print('No')
    
