import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    max_subjects = 0
    team_count = 0
    
    # n is equivalent to the number of entrants.
    for i in range(n):
        for j in range(i, n):
            subjects = 0
            # x,y for tuple combinations
            for x,y in zip(topic[i], topic[j]):
                if x=='1' or y=='1':
                    subjects += 1
            if subjects > max_subjects:
                max_subjects = subjects
                team_count = 1
            elif subjects == max_subjects:
                team_count += 1
    return [max_subjects, team_count]
                       
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
