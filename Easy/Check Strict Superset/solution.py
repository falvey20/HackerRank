A = set(input().split())
N = int(input())
result = True
for i in range(N):
    s = set(input().split())
    if not s.issubset(A):
        result = False
    if len(s) >= len(A):
        result = False
    
if result == True:
    print("True")
else:
    print("False")
