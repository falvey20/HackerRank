# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, k = input().split()
variants = list(permutations([i for i in S], int(k)))

for i in sorted(variants):
    print("".join(i))
