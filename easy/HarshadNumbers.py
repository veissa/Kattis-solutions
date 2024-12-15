"""
We’re all familiar with harshad numbers. For this problem, you will ... what’s that? You aren’t familiar with harshad numbers? They’re also known as Niven numbers – does that ring a bell?? Anything???

Well, it’s a simple enough concept. A harshad number is a number which is evenly divisible by the sum of its digits. For example,
is a harshad number: the sum of its digits is and is divisible by . is also a harshad number, since and ). is NOT a harshad number since it is not divisible by

.

OK, let’s start over.

We’re all familiar with harshad numbers. For this problem, you will be given a number
and must find the smallest harshad number

.
Input

Input consists of a single line containing a positive integer

.
Output

Display the smallest harshad number greater than or equal to
.
"""
def solved():
    n=int(input())
    while True :
        if n%(sum(int(digit) for digit in str(n)))==0:
            return n
        n+=1
print(solved())
