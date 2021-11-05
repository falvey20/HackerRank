# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
# Initiate d
d = defaultdict(list)
# Get input values for n and m
n, m = map(int, input().split())
# n+1 as 1-indexed. Append str(i) to key in dict.
for i in range(1, n+1):
    d[input()].append(str(i))
# print the values if corresponding key in dict or print -1.
for j in range(m):
    print(" ".join(d[input()]) or -1)
