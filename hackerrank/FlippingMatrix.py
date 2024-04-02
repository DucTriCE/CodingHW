#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    sum=0
    for i in range(len(matrix)//2):
        for j in range(len(matrix[0])//2):
            sum+=max(matrix[i][j],matrix[len(matrix)-i-1][j],matrix[i][len(matrix[0])-j-1], matrix[len(matrix)-i-1][len(matrix[0])-j-1])
    print(sum)

'''
1
2
112 42 83 119
56 125 56 49
15 78 101 43
62 98 114 108
'''

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        # fptr.write(str(result) + '\n')

    # fptr.close()
