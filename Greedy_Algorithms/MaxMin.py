"""
You will be given a list of integers, arr, and a single integer k.
You must create an array of length k from elements of arr such that its unfairness is minimized.
Call that array subarr.
Unfairness of an array is calculated as  max(subarr) - min(subarr)

Where:
- max denotes the largest integer in subarr
- min denotes the smallest integer in subarr

As an example, consider the array [1,4,7,2] with a k of 2. Pick any two elements, test subarr = [4,7].
unfairness = max(4,7) - min(4,7) 7-4 = 3
Testing for all pairs, the solution [1,2] provides the minimum unfairness.
"""

#!/bin/python3
# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    print(arr)
    maxMin = 0  # [10, 20, 30, 100, 200, 300, 1000]
    for i in range(0, len(arr) - k + 1):
        if i == 0:
            maxMin = arr[i + k - 1] - arr[i]
        elif maxMin > arr[i + k - 1] - arr[i]:
            maxMin = arr[i + k - 1] - arr[i]
    return maxMin


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
