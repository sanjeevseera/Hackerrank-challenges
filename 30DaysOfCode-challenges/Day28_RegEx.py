"""
Consider a database table, Emails, which has the attributes First Name and Email ID. 
Given N rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com.

Input Format

The first line contains an integer, N, total number of rows in the table. 
Each of the N subsequent lines contains 2 space-separated strings denoting a person's first name and email ID, respectively.
"""
#!/bin/python3

import re

if __name__ == '__main__':
    N = int(input())
    lists=[]
    regcom = re.compile("@gmail.com$")
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if regcom.search(emailID):
            lists.append(firstName)
    lists.sort()
    print("\n".join(lists))
