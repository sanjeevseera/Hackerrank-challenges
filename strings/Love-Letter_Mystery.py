"""
James found a love letter that his friend Harry has written to his girlfriend.
James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

He can only reduce the value of a letter by , i.e. he can change d to c, but he cannot change c to d or d to b.
The letter a may not be reduced any further.
Each reduction in the value of any letter is counted as a single operation. 
Find the minimum number of operations required to convert a given string into a palindrome.

For example, given the string , the following two operations are performed: cde -> cd-> cdc.
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    count = 0
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            count += abs(ord(s[i])-ord(s[-1-i]))
    return count

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(result)
