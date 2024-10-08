# Day 25: Running Time and Complexity
# Objective
# Today we will learn about running time, also known as time complexity.

# Task
# A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given a number, n, determine and print whether it is Prime or Not prime.

# Note: If possible, try to come up with a O(n1/2) primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code.

# Input Format
# The first line contains an integer, T, the number of test cases.
# Each of the T subsequent lines contains an integer, n, to be tested for primality.

# Constraints
# 1 <= T <= 30
# 1 <= n <= 2 x 109
# Output Format
# For each test case, print whether n is Prime or Not Prime on a new line.

# Sample Input

# 3
# 12
# 5
# 7
# Sample Output

# Not prime
# Prime
# Prime
# Explanation

# Test Case 0: n = 12.
# 12 is divisible by numbers other than 1 and itself (i.e.: 2, 3, 4, 6), so we print Not Prime on a new line.

# Test Case 1: n = 5.
# 5 is only divisible 1 and itself, so we print Prime on a new line.

# Test Case 2: n = 7.
# 7 is only divisible 1 and itself, so we print Prime on a new line.
#Solution:-

# Enter your code here. Read input from STDIN. Print output to STDOUT
from  math import sqrt
from sys import stdin
def checkPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
n = int(input())
for line in stdin:
    val = int(line)
    if (val >= 2 and checkPrime(val)):
        print("Prime")
    else:
        print("Not prime")
