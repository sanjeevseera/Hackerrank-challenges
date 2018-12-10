"""
The absolute difference between two integers, a and b, is written as |a-b|.
The maximum absolute difference between two integers in a set of positive integers, 'elements',
 is the largest absolute difference between any two integers in 'elements'.

The Difference class is started for you in the editor. It has a private integer array (elements) for storing  non-negative integers,
and a public integer (maximumDifference) for storing the maximum absolute difference.

Task
Complete the Difference class by writing the following:

A class constructor that takes an array of integers as a parameter and saves it to the 'elements' instance variable.
A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the maximumDifference instance variable.
"""


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        for i in range(len(self.__elements) - 1):
            for j in range(i + 1, len(self.__elements)):
                if abs(self.__elements[i] - self.__elements[j]) > self.maximumDifference:
                    self.maximumDifference = abs(self.__elements[i] - self.__elements[j])
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)