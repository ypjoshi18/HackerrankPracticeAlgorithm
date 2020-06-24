#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    temp = scores[0]
    mcount=0
    lcount=0
    for i in range(len(scores)):
        if (temp < scores[i]):
            temp = scores[i]
            mcount+=1
    temp = scores[0]
    for i in range(len(scores)):
        if (temp > scores[i]):
            temp = scores[i]
            lcount+=1
    return (mcount,lcount)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
