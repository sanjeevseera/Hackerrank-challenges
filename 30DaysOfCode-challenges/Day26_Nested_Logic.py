"""
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0).
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine=15*(no of days late).
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine=500*(no of months late).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000.
"""

RD = list(map(int,input().split(" ")))
AD = list(map(int,input().split(" ")))
if AD[-1] < RD[-1]:
    print(10000)
elif AD[-1] == RD[-1] and AD[1] < RD[1]:
    print((RD[1]-AD[1])*500)
elif AD[-1] == RD[-1] and AD[1] == RD[1] and AD[0] < RD[0]:
    print((RD[0]-AD[0])*15)
else:
    print(0)

