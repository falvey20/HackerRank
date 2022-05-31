cube = lambda x: x**3 

def fibonacci(n):
    nums = []
    n1, n2 = 0, 1
    while len(nums) != n:
        nums.append(n1)
        if len(nums) != n:
            nex = n1 + n2
            n1 = n2
            n2 = nex
    return nums
