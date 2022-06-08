from itertools import product
K, M = map(int, (input().split()))
lists = []
for i in range(K):
    lists.append(list(map(int, input().split()[1:])))
options = list(product(*lists))

result = 0
for i in options:
    total = sum([element ** 2 for element in i]) % M
    if total > result:
        result = total
print(result)
