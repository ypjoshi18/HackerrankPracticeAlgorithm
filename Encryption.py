#!/bin/python3

import math
import os
import random
import re
import sys
from math import *

# Complete the encryption function below.
def encryption(s):
    n = len(s)
    r = floor(sqrt(n))
    c = ceil(sqrt(n))
    res = []
    for i in range(c):
        j=0
        temp=[]
        while i+j<n:
            temp.append(s[i+j])
            j+=c
        res.append("".join(temp))
    return " ".join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
