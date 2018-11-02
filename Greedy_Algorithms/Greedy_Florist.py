"""
A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new customers and the money he makes.
To do this, he decides he'll multiply the price of each flower by the number of that customer's previously purchased flowers plus 1.
The first flower will be original price, (0+1) original price, the next will be (1+1) original price and so on.

Given the size of the group of friends, the number of flowers they want to purchase and the original prices of the flowers,
determine the minimum cost to purchase all of the flowers.

For example, if there are k=3 friends that want to buy n=4 flowers that cost c=[1,2,3,4] each will buy one of the flowers priced [2,3,4]
 at the original price. Having each purchased x=1 flower, the first flower in the list, c[0], will now cost
 (current purchase + previous purchase)*c[0]=(1+1)*1=2.
  The total cost will be 2+3+4+2=11.
"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    sum = 0
    j = 0
    for i in range(0, len(c), k):
        if i + k <= len(c):
            last = i + k
        else:
            last = len(c)
        for n in range(i, last):
            sum += (j + 1) * c[n]
        j += 1
    return sum


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)


