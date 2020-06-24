#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    arr = []
    aInString = 0
    leftOverCount = 0
    timesRan = (int)(n/len(s))
    leftOver = n%len(s)
    arr=s[0:leftOver]
    #for every char in the s check count the a's
    for i in range(len(s)):
        if s[i] == 'a':
            aInString +=1
        
        #adds leftover count while checking for how many a's in reg count
        if i < len(arr) and s[i] =='a':
            leftOverCount +=1
            
    return timesRan*aInString + leftOverCount
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
