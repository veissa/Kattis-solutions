"""
Little Jóna needs a program. The program should read integers and print them in reverse order. Jóna asks for your help.
Input

The first line of input contains the integer
. Then comes a list of

integers, each on its own line.
Output

The list should be printed in reverse order of input.

"""


n=int(input())
list=[]
for i in range(n):
    list=[input()]+list
for i in list:
    print(i)
