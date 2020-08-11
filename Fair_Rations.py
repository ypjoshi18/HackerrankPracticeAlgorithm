#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    n = len(B)
    breads = 0
    for i in range(n-1):
        if B[i] % 2 == 1:
            breads += 2
            B[i+1] += 1
    if B[n-1] % 2 == 1:
        return "NO"
    else:
        return breads

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
