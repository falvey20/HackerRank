from itertools import combinations_with_replacement

STDIN = input()
s, k = sorted(STDIN.split()[0]), int(STDIN.split()[1])

combos = combinations_with_replacement(s, k)
for i in combos:
    print(''.join(i))
