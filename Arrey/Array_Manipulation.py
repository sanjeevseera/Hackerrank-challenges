"""
Input Format

The first line contains two space-separated integers n and m, the size of the array and the number of operations. 
Each of the next m lines contains three space-separated integers a, b and k, the left index, right index and summand.

Output Format

Return the integer maximum value in the finished array.

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output

200
Explanation

After the first update list will be 100 100 0 0 0. 
After the second update list will be 100 200 100 100 100. 
After the third update list will be 100 200 200 200 100. 
The required answer will be 200.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    nlist = [0]*(n+1)
    for qi in queries:
        x, y, incr = qi
        nlist[x-1] += incr
        if((y)<=len(nlist)): 
            nlist[y] -= incr;
    rmax =  tmax= 0
    for i in nlist:
        tmax=tmax+i;
        if(rmax < tmax): 
            rmax = tmax
    return rmax

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    print(result)
