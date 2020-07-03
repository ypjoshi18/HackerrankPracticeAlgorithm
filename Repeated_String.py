#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    m = s.count('a')
    if m==0:
        return 0
    elif m==1 and len(s)==1:
        return n
    else:
        r=int(n/len(s))
        rr=int(n%len(s))
        return(m*r+s[:rr].count('a'))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
