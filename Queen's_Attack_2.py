#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r, c, obstacles):
    left = c-1
    right = n-c
    up = n-r
    down = r-1
    upleft    = left if up >= left else up
    upright   = right if up >= right else up
    downleft  = left if down >= left else down
    downright = right if down >= right else down

    for obst in obstacles:
        row = obst[0]
        col = obst[1]

        if row ==r and col < c:
            if c-col-1 < left:
                left = c-col-1
        
        elif row ==r and col > c:
            if col - c -1 < right:
                right = col-c-1

        elif row > r and col == c:
            if row - r-1 < up :
                up = row -r-1
        
        elif row < r and col == c:
            if r-row-1 < down:
                down = r-row-1

        elif col < c and row > r:
            if row-r == c-col:
                if row-r-1 < upleft:
                    upleft = row-r-1
            
        elif col > c and row > r:
            if col-c == row-r:
                if row -r-1 <upright:
                    upright= row-r-1
        
        elif row < r  and col < c:
            if c-col == r -row:
                if r-row-1 < downleft:
                    downleft = r-row-1
            
        elif row < r and col> c:
            if r -row == col -c:
                if r-row-1 < downright:
                    downright = r-row-1

    attack = up + right + left + down + upright + upleft + downright + downleft
    return attack




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
