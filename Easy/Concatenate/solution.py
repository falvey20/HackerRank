import numpy

N, M, P = map(int, input().split())
n = numpy.array([input().split() for i in range(N)], int)
m = numpy.array([input().split() for i in range(M)], int)
print(numpy.concatenate((n, m)))
    
