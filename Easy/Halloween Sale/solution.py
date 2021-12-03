import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    games_bought = 0
    # Set next price
    next_price = p
    # While next price is more than minimum price
    # if enough money left, buy game and update next price by deducting d
    while next_price > m:
        if s >= next_price:
            games_bought += 1
            s -= next_price
            next_price -= d
        # If insufficient funds to buy next game, return games bought
        else:
            return games_bought
    # Establish how many more games can be bought with remaining money at miniumum price
    games_bought += math.floor(s/m)
    return games_bought
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
