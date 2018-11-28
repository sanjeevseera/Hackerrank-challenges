#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    i = 0
    j = len(s)-1
    dl = False
    res = -1
    while i < j:
        if dl and (s[i] != s[j]):
            res = -1
            break
        elif s[i] == s[j]:
            i += 1
            j -= 1
        elif not dl and (s[i+1] == s[j]):
            if (i+2 < j+1) and (s[i+2] == s[j-1]):
                res = i
                i += 3
                j -= 2
                dl = True
            elif (i+2 < j+1) and (s[i+2] != s[j-1]) and s[i] == s[j-1]:
                res = j
                i +=1
                j -= 2
                dl = True
            else:
                res = i
                i += 2
                j -= 1
                dl = True
        elif not dl and (s[i] == s[j-1]):
            res = j
            i +=1
            j -= 2
            dl = True
        else:
            res = -1
            break
    return res

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(result)

