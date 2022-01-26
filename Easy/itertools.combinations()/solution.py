from itertools import combinations

Sk = input().split()
S = Sk[0]
k = int(Sk[1])

for i in range(1, k+1):
    for j in combinations(sorted(S),i):
        print("".join(j))
