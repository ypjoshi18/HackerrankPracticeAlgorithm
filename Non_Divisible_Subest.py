#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, arr):
    resid_cnt = [0] * k
    
    for el in arr:
        resid_cnt[el%k] += 1
        
    res = min(1, resid_cnt[0])
    for ind in range(1, (k//2)+1):
        if ind != k - ind:
            res += max(resid_cnt[ind], resid_cnt[k - ind])
    
    if k % 2 == 0 and resid_cnt[int(k/2)] != 0:
        res += 1
    
    return res
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
