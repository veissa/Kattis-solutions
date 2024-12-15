"""
Now one’s goose is cooked and the raw carrots are smoked!

Per-Magnus’ boss stormed into his office and complained about the addition program you had written for him previously. It can only add two numbers, which is of course completely unusable! How could you even come up with such a silly idea?

Fix your program posthaste, so that it instead sums up
integers for a given

.
Input

The first line of the input contains an integer
(

), the number of integers your program should add.

The next line contains the
integers to add, each between and

.
Output

Output a single integer – the sum of the
integers from the input.
"""
N=int(input())
line=input().split()
s=0
for i in line:
    s+=int(i)
print(s)
