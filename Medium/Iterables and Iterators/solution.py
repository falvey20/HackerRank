from itertools import combinations

N = int(input())
letters = input().split(" ")
K = int(input())

choices = list(combinations(letters, K))
contains = 0
for i in choices:
    if 'a' in i:
        contains += 1

print(contains/len(choices))
