import numpy

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

print(numpy.transpose(arr))
print(numpy.array(arr).flatten())
