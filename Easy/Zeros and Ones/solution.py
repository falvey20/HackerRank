import numpy

nums = tuple(int(i) for i in input().split(" "))

print(numpy.zeros(nums, dtype = int))
print(numpy.ones(nums, dtype = int))
