"""
Given 'n' names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each 'name' queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
if an entry for 'name' is not found, print Not found instead.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = {}
for i in range(n):
    s = input().split(" ")
    d[s[0]] = s[1]

#print(d)
while True:
    try:
        s = input()
        if s in d.keys():
            print(s+"="+d[s])
        else:
            print("Not found")
    except EOFError:
        break

