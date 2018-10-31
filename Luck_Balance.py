"""
Complete the luckBalance function in the editor below. It should return an integer that represents the maximum luck balance achievable.

luckBalance has the following parameter(s):

k: the number of important contests Lena can lose
contests: a 2D array of integers where each contest[i] contains two integers that represent the luck balance and importance of the Ith contest.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    implist = []
    unimplist = []
    luck = 0
    for i in contests:
        luck += i[0]
        if i[1] == 0:
            unimplist.append(i[0])
        else:
            implist.append(i[0])
    implistcount=len(implist)
    implist.sort()
    for n in range(implistcount-k):
        luck -= 2*implist[n]
    return luck

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    print(result)
