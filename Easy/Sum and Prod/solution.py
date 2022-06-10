import numpy

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
numparr = numpy.array(arr)
print(numpy.prod(numpy.sum(numparr, axis=0)))
