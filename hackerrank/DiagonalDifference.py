#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
'''
3
11 2 4
4 5 6
10 8 -12
'''

def diagonalDifference(arr):
    left_to_right, right_to_left = 0, 0
    left_to_right = [row[i-1]  for i, row in enumerate(arr, start=1)]
    right_to_left = [row[-i]  for i, row in enumerate(arr, start=1)]
    print(abs(sum(left_to_right)-sum(right_to_left)))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
