#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    tracker = 0
    count = 0
    aboveSea = True
    for i in s:
        if i == 'D':
            tracker -= 1
        elif i == 'U':
            tracker += 1
        if aboveSea and tracker < 0:
            count += 1
            aboveSea = False
        if tracker >= 0:
            aboveSea = True
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
