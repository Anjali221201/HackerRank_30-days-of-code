# # Day 10: Binary Numbers
# Objective
# Today, we’re working with binary numbers.

# Task
# Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1‘s in n‘s binary representation. When working with different bases, it is common to show the base as a subscript.

# Example

# n = 125

# The binary representation of 12510 is 11111012. In base 10, there are 5 and 1 consecutive ones in two groups. Print the maximum, 5.

# Input Format
# A single integer, n.

# Constraints
# 1 <= n <= 106
# Output Format
# Print a single base-10 integer that denotes the maximum number of consecutive 1‘s in the binary representation of n.

# Sample Input 1

# 5
# Sample Output 1

# 1
# Sample Input 2

# 13
# Sample Output 2

# 2
# Explanation

# Sample Case 1:
# The binary representation of 510 is 1012, so the maximum number of consecutive 1‘s is 1.

# Sample Case 2:
# The binary representation of 1310 is 11012, so the maximum number of consecutive 1‘s is 2.
#Solution:-
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    binary_representation = bin(n)[2:]
    
    ones_sequences = binary_representation.split('0')
    
    max_consecutive_ones = max(len(seq) for seq in ones_sequences)

    print(max_consecutive_ones)
