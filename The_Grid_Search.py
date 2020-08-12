#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):

    def check(x,y):
        for i in range(r):
            if P[i] != G[x+i][y:y+c]:
                return False
        return True


    for i in range(R):
        for j in range(C):
            if G[i][j]== P[0][0]:
                if check(i,j):
                    return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
