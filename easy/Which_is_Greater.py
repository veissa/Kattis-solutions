"""
Given two positive integers, determine whether the first one is larger than the second one.
Input

The single line of input contains two positive integers,
and (

).
Output

Output a single line with 1 if
, 0 otherwise.
"""
n=input()
a,b = n.split(" ")
if int(a)>int(b):
    print(1)
else : print(0)
