N, n = int(input()), input().split()
if all(int(i) > 0 for i in n) and any(i == i[::-1] for i in n):
    print("True")
else:
    print("False")
