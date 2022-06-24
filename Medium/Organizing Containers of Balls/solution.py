import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # total balls in each bucket
    balls_in_each_bucket = [sum(i) for i in container]
    # total balls of each colour
    total_of_each_colour = []
    for i in range(len(container)):
        count = 0
        for j in range(len(container)):
            count += container[j][i]
        total_of_each_colour.append(count)
    
    if sorted(balls_in_each_bucket) == sorted(total_of_each_colour):
        return "Possible"
    return "Impossible"
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
