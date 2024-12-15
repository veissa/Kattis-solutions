"""
Some numbers are just, well, odd. For example, the number is odd, because it is not a multiple of two. Numbers that are a multiple of two are not odd, they are even. More precisely, if a number can be expressed as for some integer , then is even. For example,

is even.

Some people get confused about whether numbers are odd or even. To see a common example, do an internet search for the query “is zero even or odd?” (Don’t search for this now! You have a problem to solve!)

Write a program to help these confused people.
Input

Input begins with an integer
on a line by itself, indicating the number of test cases that follow. Each of the following lines contain a test case consisting of a single integer

.
Output

For each
, print either ‘ is odd’ or ‘ is even’ depending on whether is odd or even.
"""




n=int(input())
array=[]
for i in range(n):
    array.append(int(input()))
for i in array :
    if abs(i)%2==0:
        print(f"{i} is even")
    else :
        print(f"{i} is odd")
