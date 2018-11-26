#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    for i in range(len(q) - 1, 0, -1):
        if q[i] == i + 1:
            continue
        else:
            j = q.index(i + 1)
            if i - j > 2:
                print("Too chaotic")
                return
            count += i - j
            q = q[:j] + q[j + 1:] + q[j:j]
    print(count)
    return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
