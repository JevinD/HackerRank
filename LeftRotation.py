#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    arr=a
    #number of rotations
    for rotations in range(d):
        #holds the last number of the array
        temp=arr[0]
        #rotates array once
        for i in range(len(a)-1):
            arr[i] = arr[i+1]
        arr[len(a)-1] = temp
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
