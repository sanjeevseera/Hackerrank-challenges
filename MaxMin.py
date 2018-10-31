#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    print(arr)
    maxMin = 0  # [10, 20, 30, 100, 200, 300, 1000]
    for i in range(0, len(arr) - k + 1):
        if i == 0:
            maxMin = arr[i + k - 1] - arr[i]
        elif maxMin > arr[i + k - 1] - arr[i]:
            maxMin = arr[i + k - 1] - arr[i]
    return maxMin


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
