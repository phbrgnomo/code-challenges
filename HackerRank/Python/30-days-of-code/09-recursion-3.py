#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):

    return 1 if n <= 1 else n * factorial(n-1)
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    n = 4
    result = factorial(n)
    print(result)
    
    # fptr.write(str(result) + '\n')

    # fptr.close()
