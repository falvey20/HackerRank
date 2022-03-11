eng = int(input())
eng_c = set(map(int, input().split(" ")))
fre = int(input())
fre_c = set(map(int, input().split(" ")))

print(len(eng_c.union(fre_c)))
