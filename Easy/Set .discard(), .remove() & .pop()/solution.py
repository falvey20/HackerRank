n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    x = input()
    if x == 'pop':
        s.pop()
    else:
        if x.split(" ")[0] == 'remove':
            s.remove(int(x.split(" ")[1]))
        elif x.split(" ")[0] == 'discard':
            s.discard(int(x.split(" ")[1]))
            
print(sum(s))
    
