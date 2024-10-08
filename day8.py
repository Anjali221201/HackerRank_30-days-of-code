#Topic : Dictionaries and Maps
# Task
# Given n names and phone numbers, assemble a phone book that maps friends’ names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.

# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

# Input Format
# The first line contains an integer, n, denoting the number of entries in the phone book.
# Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line. The first value is a friend’s name, and the second value is an 8-digit phone number.

# After the n lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.

# Note: Names consist of lowercase English alphabetic letters and are first names only.

# Constraints
# 1 <= n <= 105
# 1 <= queries <= 105
# Output Format
# On a new line for each query, print Not found if the name has no corresponding entry in the phone book; otherwise, print the full name and phoneNumber in the format name=phoneNumber.

# Sample Input
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry
# Sample Output
# sam=99912222
# Not found
# harry=12299933
# Explanation
# We add the following n = 3 (Key,Value) pairs to our map so it looks like this:

# phoneBook = {(sam, 99912222), (tom, 11122222), (harry, 12299933)}
# Step 1: Read the number of entries
n = int(input())

# Step 2: Create an empty dictionary to store the phone book
phone_book = {}

# Step 3: Read the name and phone number pairs
for _ in range(n):
    entry = input().split()
    if len(entry) == 2:
        name, phoneNumber = entry
        phone_book[name] = phoneNumber

# Step 4: Process the queries
while True:
    try:
        user_input = input()
        if user_input in phone_book:
            print(f"{user_input}={phone_book[user_input]}")
        else:
            print("Not found")
    except EOFError:
        break
