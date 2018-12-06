"""
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum
number of consecutive 1's in n's binary representation.
"""

n = int(input())
bn = "{0:b}".format(n)
print(bn)
for i in range(len(bn), 0, -1):
    if "1" * i in bn:
        print(i)
        break
else:
    print(0)