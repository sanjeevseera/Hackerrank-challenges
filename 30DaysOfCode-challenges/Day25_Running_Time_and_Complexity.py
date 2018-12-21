"""
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
Given a number, 'n', determine and print whether it's 'Prime' or 'Not Prime'.

Note: If possible, try to come up with a O(sqrt(n)) primality algorithm, or see what sort of optimizations you come up with for an O(n) algorithm. 
Be sure to check out the Editorial after submitting your code!
"""

from math import sqrt

def prime(n):
    if n==1:
        return "Not prime"
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return "Not prime"
    return "Prime"

T = int(input())
for _ in range(T):
    n = int(input())
    print(prime(n))
