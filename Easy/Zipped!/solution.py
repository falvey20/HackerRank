N, X = map(int, input().split(' '))

marks = []
for i in range(X):
    marks.append(list(float(mark) for mark in input().split(' ')))

for i in zip(*marks):
    print(sum(i)/X)
    
