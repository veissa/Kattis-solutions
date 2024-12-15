"""
The factorial of , written as , is defined as the product of all the integers from to . For example,

.

This number can be very large, so instead of computing the entire product, just compute the last digit of
(when is written in base 

).
Input

The first line of input contains a positive integer
, the number of test cases. Each of the next lines contains a single positive integer . is at most

.
Output

For each value of
, print the last digit of .
"""
n=int(input())
answer=[]
for i in range(n):
    answer.append(int(input()))
for i in answer:
    if i==1:
        print(1)
    elif i==2:
        print(2)
    elif i==3:
        print(6)
    elif i==4:
        print(4)
    else : print(0)
