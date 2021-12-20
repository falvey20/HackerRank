import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    stations = sorted(c)
    # print(stations)
    
    start = stations[0] - 0
    end = (n-1) - stations[-1]
    
    max_distance = max(start, end)
    
    for i in range(0, len(stations)-1):
        distance = abs(stations[i] - stations[i+1])//2
        # print(distance)
        if distance > max_distance:
            max_distance = distance
    
    return max_distance
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
