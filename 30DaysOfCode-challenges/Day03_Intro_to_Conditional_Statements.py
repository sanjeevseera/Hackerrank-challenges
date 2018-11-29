
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N%2 == 1 or N >= 6 and N <=20:
        print("Weird")
    elif N<=5 or N>20:
        print("Not Weird")