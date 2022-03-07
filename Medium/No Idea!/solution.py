mn = input().split()
m = int(mn[0])
n = int(mn[1])
arr = [int(i) for i in input().split()]
a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])

happiness = 0

for num in arr:
    if num in a:
        happiness += 1
    if num in b:
        happiness -= 1

print(happiness)
