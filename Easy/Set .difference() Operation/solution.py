eng = int(input())
engroll = set([i for i in input().split(' ')])
fre = int(input())
freroll = set([i for i in input().split(' ')])

engonly = len(engroll.difference(freroll))
print(engonly)
