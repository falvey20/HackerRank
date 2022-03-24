M = int(input())
m = set(list(map(int, input().split(" "))))
N = int(input())
n = set(list(map(int, input().split(" "))))

md = m.difference(n)
nd = n.difference(m)
mdnd = md.union(nd)

for i in sorted(list(mdnd)):
    print(i)
