"""
Given set S={1,2,3,..,N}. Find two integers, A and B (where A<B), 
from set S such that the value of A&B is the maximum possible and also less than a given integer, K.
In this case, & represents the bitwise AND operator.

Input Format

The first line contains an integer, T, the number of test cases. 
Each of the T subsequent lines defines a test case as 2 space-separated integers, N and K, respectively.
"""
#!/bin/python3

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        if (k-1 | k) <= n:
            print(k-1)
        else:
            print(k-2)


