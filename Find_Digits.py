#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    new = str(n)
    temp = 0
    count = 0
    for i in range(len(new)):
        if (int(new[i])!=0):
            if(int(new) % int(new[i]) == 0):
                count+=1
    return count     


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
