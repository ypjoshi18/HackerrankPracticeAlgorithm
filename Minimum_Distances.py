#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    temp= []
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                temp.append(j-i)
    if len(temp)==0:
        return -1
    return min(temp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
