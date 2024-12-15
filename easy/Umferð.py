"""
Traffic jams are a major problem in larger cities like Njú Jork and Síattúl, especially during rush hour.

In a traffic jam there are many cars with very little spacing between them, and they are not moving particularly fast. To simplify things we will assume that traffic is divided into lanes and each lane consists of
cells. Each cell can contain at most

car, but a cell can also be empty.

The length
of the lanes, the number of lanes and a textual description of each cell, such that a cell containing a car is denoted # and an empty cell is denoted ., is given.
The task at hand is to calculate the proportion of empty cells, as a number between and

, inclusive.
Input

The first line of the input contains a single integer
, the number of cells per lane. The next line contains a single integer , the number of lanes. Next there are lines. Each line contains

letters, each being either . or #.
OutputPrint the proportion of empty cells as a value from to

.

The output is considered correct if its relative or absolute error is at most
. This means that the exact number of digits after the decimal point does not matter as long as the value is accurate enough.
"""
m=int(input())
n=int(input())
empty=0
for i in range(n):
    empty+=input().count(".")
answer=float(empty)/float(m*n)
print(answer)
