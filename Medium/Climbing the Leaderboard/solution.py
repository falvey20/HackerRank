import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    result = []
    # scores is sorted set of ranked
    scores = sorted(set(ranked))
    l = len(scores)
    # i acts as placeholder in scores
    i = 0
    for new_score in player:
        # while i hasnt been through all ranked scores
        # and current ranked score is less or equal to player score
        while i < l and scores[i] <= new_score:
            i += 1
        result.append((l-i)+1)
        
    return result
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
