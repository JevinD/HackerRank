#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    size = len(arr)

    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n +=1
        else:
            z+=1
    print(p/size)
    print(n/size)
    print(z/size)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
