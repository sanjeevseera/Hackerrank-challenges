"""
Given an array, 'a', of size 'n' distinct elements, sort the array in ascending order using the Bubble Sort algorithm above.
Once sorted, print the following '3' lines:

Array is sorted in numSwaps swaps.
where 'numSwaps' is the number of swaps that took place.
First Element: firstElement
where 'FirstElement' is the first element in the sorted array.
Last Element: lastElement
where 'lastElement' is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during
"""

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
noofswaos = 0

for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
            noofswaos +=1

print("Array is sorted in {} swaps.".format(noofswaos))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))