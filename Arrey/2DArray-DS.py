"""
For example, given the 2D array:

-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
We calculate the following 16 hourglass values:

-63, -34, -9, 12,
-10, 0, 28, 23,
-27, -11, -2, 10,
9, 17, 25, 18
Our highest hourglass value is 28 from the hourglass:

0 4 3
  1
8 6 6
"""
#!/bin/python3
# Complete the hourglassSum function below.
def hourglassSum(arr):
    if len(arr) < 3 or len(arr[0]) < 3:
        return 0
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            temp = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if (i==0 and j==0) or temp > tmax:
                tmax = temp
    return tmax

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print(result)
