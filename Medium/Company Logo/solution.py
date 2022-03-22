from collections import Counter

import math
import os
import random
import re
import sys

def most_common(s):
    counts = Counter(sorted(s)).most_common(3)
    return counts
    

if __name__ == '__main__':
    s = input()
    for _ in most_common(s):
        print(str(_[0]) + " " + str(_[1]))
