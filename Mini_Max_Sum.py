#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_sum = (sum(arr)-max(arr))
    max_sum = (sum(arr)-min(arr))
    print (min_sum, max_sum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
