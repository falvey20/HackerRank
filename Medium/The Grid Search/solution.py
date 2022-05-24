import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    gh, gw, ph, pw = len(G), len(G[0]), len(P), len(P[0])
    for i in range(0, (gh-ph)+1):
        for j in range(0, (gw-pw)+1):
            if G[i][j:j+pw] == P[0]:
                subgrid = []
                for k in range(i, i+ph):
                    subgrid.append(G[k][j:j+pw])
                if subgrid == P:
                    return "YES"
    return "NO"
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
