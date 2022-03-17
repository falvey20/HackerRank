import re

N = int(input())

for _ in range(N):
    num = input()
    if re.search('[a-zA-Z]', num):
        print("NO")
    elif len(num) == 10 and num[0] in ('7', '8', '9'):
        print("YES")
    else:
        print("NO") 
