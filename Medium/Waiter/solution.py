import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def gen_primes(count):
    primes = []
    num = 2
    while len(primes) != count:
        isprime = True
        for x in range(2, int(math.sqrt(num) + 1)):
            if num % x == 0: 
                isprime = False
                break
        if isprime:
            primes.append(num)
        num += 1
    return primes
        

def waiter(number, q):
    primes = gen_primes(q)
    answers = []
    A = []
    B = []
    
    for i in range(q):
        while number:
            value = number.pop()
            if value % primes[i] == 0:
                B.append(value)
            else:
                A.append(value)
        while B:
            answers.append(B.pop())
        number = A
        A = []
    
    while number:
        answers.append(number.pop())
    return answers
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
