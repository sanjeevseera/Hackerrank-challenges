"""
Two words are anagrams of one another if their letters can be rearranged to form the other word.

In this challenge, you will be given a string. You must split it into two contiguous substrings,
then determine the minimum number of characters to change to make the two substrings into anagrams of one another.

For example, given the string 'abccde', you would break it into two parts: 'abc' and 'cde'.
Note that all letters have been used, the substrings are contiguous and their lengths are equal.
Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams.
Two changes were necessary.

Function Description

Complete the anagram function in the editor below.
It should return the minimum number of characters to change to make the words anagrams, or -1 if it's not possible.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if len(s)%2 == 1:
        return -1
    else:
        l1 = list(s[:len(s)//2])
        l2 = list(s[len(s)//2:])
        l1.sort()
        l2.sort()
        i = 0
        while True:
            if i >= len(l1):
                break
            elif l1[i] in l2:
                c = l1[i]
                while (c in l1) and (c in l2):
                    l2.remove(c)
                    l1.remove(c)
            else:
                i+=1
        return len(l1)


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(result)