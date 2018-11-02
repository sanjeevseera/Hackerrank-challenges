"""
Function Description

Complete the minimumAbsoluteDifference function in the editor below.
It should return an integer that represents the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

n: an integer that represents the length of arr
arr: an array of integers
"""

#!/bin/python3

import os
# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if i ==0:
            res = abs(arr[i]-arr[i+1])
        elif abs(arr[i]-arr[i+1]) < res:
            res = abs(arr[i]-arr[i+1])
        else:
            pass
    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)
