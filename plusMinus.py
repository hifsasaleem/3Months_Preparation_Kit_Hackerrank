import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    size = len(arr)
    pnum = 0
    nnum = 0
    zero = 0
    for num in range(size):
        if arr[num] > 0:
            pnum += 1
        elif arr[num] < 0:
            nnum += 1
        else:
            zero += 1
    print("{0:.6f}".format(pnum/size))
    print("{0:.6f}".format(nnum/size))
    print("{0:.6f}".format(zero/size))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
