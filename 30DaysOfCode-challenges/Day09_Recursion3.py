"""
Write a factorial function that takes a positive integer, N as a parameter and prints the result of N!(N factorial).
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    n = int(input())

    print(factorial(n))
