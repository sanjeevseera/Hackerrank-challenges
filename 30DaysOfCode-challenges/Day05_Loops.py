"""
Task
Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.
"""

#!/bin/python3
if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
        print("{} x {} = {}".format(n,i,n*i))