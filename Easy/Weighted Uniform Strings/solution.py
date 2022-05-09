import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    values = []
    last = ''
    for i in range(len(s)):
        char = s[i]
        val = ord(char) - 96
        if last == '':
            last = char
            values.append(val)
        elif last[-1] == char:
            last += char
            values.append(val*len(last))
        elif last != char:
            last = char
            values.append(val)
    values = set(values)
    result = []
    for i in queries:
        if i in values:
            result.append("Yes")
        else:
            result.append("No")
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
