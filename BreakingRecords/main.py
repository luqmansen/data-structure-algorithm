#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    lowest_curr, highest_curr = scores[0], scores[0]
    lowest_cnt = 0
    highest_cnt = 0
    for i, v in enumerate(scores):
        if v < lowest_curr:
            lowest_cnt += 1
            lowest_curr = v
        elif v > highest_curr:
            highest_curr = v
            highest_cnt += 1

    return lowest_cnt, highest_cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))
    # scores = [10,5,20, 20, 4, 5, 2, 25, 1]
    # scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
