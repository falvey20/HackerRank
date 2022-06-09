import numpy

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
numpyarr = numpy.array(arr)

print(max(numpy.min(numpyarr, axis=1)))
