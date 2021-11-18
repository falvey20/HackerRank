import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    new_grid = []
    l = len(grid)
    # Iterate over each row in grid
    for i in range(0, l):
        # If row is top or bottom row, append to new grid
        if i == 0 or i == l-1:
            new_grid.append(list(grid[i]))
        else:
            row = []
            # Append Left border to new row
            row.append(grid[i][0])
            # Iterate through each grid row and check against surrounding values.
            for j in range(1, l-1):
                if grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i][j+1]:
                    row.append('X')
                else:
                    row.append(grid[i][j])
            # Append Right border to new row
            row.append(grid[i][l-1])
            new_grid.append(row)
    # Return new_grid as a list of strings (rather than list of lists)    
    return map(''.join, new_grid)
              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
