#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    count = 0
    for i in range(a,b+1):
        if(issquare(i)):
            count+=1
    return count

def issquare(x):
    sr = math.sqrt(x) 
    return ((sr - math.floor(sr)) == 0)     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
