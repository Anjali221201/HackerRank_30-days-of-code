# Day 9: Recursion
# Objective
# Today, we are learning about an algorithmic concept called recursion.

# Function Description
# Complete the factorial function in the editor below. Be sure to use recursion.

# factorial has the following paramter:

# int n: an integer
# Returns

# int: the factorial of n
# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

# Input Format
# A single integer, n (the argument to pass to factorial).

# Constraints
# 2 <= n <= 12
# Your submission must contain a recursive function named factorial.
# Sample Input

# 3
# Sample Output

# 6
# Explanation

# Consider the following steps. After the recursive calls from step 1 to 3, results are accumulated from step 3 to 1.

# factorial(3) = 3 x factorial(2) = 3 x 2 = 6
# factorial(2) = 2 x factorial(2) = 2 x 1 = 2
# factorial(1) = 1
#Solution:-
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
    # Write your code here
    if n==1 or n<=0:
        return 1
    else:
        return n*factorial(n-1)
        

if __name__ == '__main__':

    n = int(input().strip())

    result = factorial(n)
    print(result)

