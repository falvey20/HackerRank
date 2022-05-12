a = int(input())
A = set(input().split())

n = int(input())
for i in range(n):
    op_l = input().split()
    N = set(input().split())
    if op_l[0] == "update":
        A.update(N)
    elif op_l[0] == "intersection_update":
        A.intersection_update(N)
    elif op_l[0] == "symmetric_difference_update":
        A.symmetric_difference_update(N)
    elif op_l[0] == "difference_update":
        A.difference_update(N)

print(sum(map(int, A)))
