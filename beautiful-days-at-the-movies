#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for num in range(i,j+1):
        rev=reverseDigits(num)
        print((abs(num-rev)))
        if (abs(num-rev)%k)== 0:
            count+=1
    return count

#reverses the Digits
def reverseDigits(num): 
    rev = 0
    while(num > 0): 
        a = num % 10
        rev = rev * 10 + a 
        num = num // 10
    return rev

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
