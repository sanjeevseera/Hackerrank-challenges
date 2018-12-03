"""
Given a string, S, of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for _ in range(n):
    s = input()
    s1 = ""
    s2 = ""
    for i in range(len(s)):
        if i%2 == 0:
            s1 += s[i]
        else:
            s2 += s[i]
    print(s1+" "+s2)
