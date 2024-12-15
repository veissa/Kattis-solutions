"""
Young Mirko threw matches all over the floor of his room.

His mom did not like that and ordered him to put all the matches in a box. Mirko soon noticed that not all of the matches on the floor fit in the box, so he decided to take the matches that don’t fit and throw them in the neighbour’s garbage, where his mom (hopefully) won’t find them.

Help Mirko determine which of the matches fit in the box his mom gave him. A match fits in the box if its entire length can lie on the bottom of the box. Mirko examines the matches one by one.
Input

The first line of input contains an integer
(), the number of matches on the floor, and two integers and , the dimensions of the box (,

).

Each of the following
lines contains a single integer between and

(inclusive), the length of one match.
Output

For each match, in the order they were given in the input, output on a separate line “DA” if the match fits in the box or “NE” if it does not.
Sample Input 1 	
5 3 4
3
4
5
6
7

Sample Output 1
	

DA
DA
DA
NE
NE

Sample Input 2 	

2 12 17
21
20

Sample Output 2

NE
DA
"""

import math

n, a, b = map(int, input().split())

diagonal = math.sqrt(a**2 + b**2)

for _ in range(n):
    match_length = int(input())
    if match_length <= diagonal:
        print("DA")
    else:
        print("NE")
