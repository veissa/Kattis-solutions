"""
In the United States of America, telephone numbers within an area code consist of seven digits: the prefix number is the first three digits and the line number is the last four digits. Traditionally, the

prefix number has been used to provide directory information and assistance as in the following examples:

    555-1212

    555-9876

    555-5000

    555-7777

Telephone company switching hardware would detect the
prefix and route the call to a directory information operator. Nowadays, telephone switching is done digitally and somewhere along the line a computer decides where to route calls.
For this problem, write a program that determines if a supplied seven-digit telephone number should be routed to the directory information operator, that is, the prefix number is

.
Input

The single line of input contains a single integer
(

), which is a telephone number.
Output

Output a single integer, which is
if the number should be routed to the directory information operator, or if the number should not be routed to the directory information operator.
""""

s=input()
if s[:3]=="555":
    print(1)
else : print(0)
