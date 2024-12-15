"""
Jónas’s birthday is tomorrow and he is trying to decide whether to have a party. One of Jónas’s new year resolutions was to only have parties if it’s a big anniversary, those being every ten years.

Given the age Jónas is turning tomorrow, reply whether it is a big anniversary or not.
Input

The input is a single line containing an integer
(

), Jónas’s age in years.
Output

Print Jebb if it’s a big anniversary, print Neibb otherwise.
"""




age=int(input())
if age%10==0 : print("Jebb")
else : print("Neibb")
