"""
Sigrún got a lot of presents from all the guests that attended her birthday party today. She has opened all the gifts and noticed that they weren’t equally fun.

She made a list of all the gifts she got, from whom she got each gift and a number denoting how much she enjoyed the gift — the higher the number, the more fun the gift is.

Can you help Sigrún find who gave her the most fun gift?
Input
The first line contains a single integer (), the number of guests who attended the party and gave Sigrún a gift. Then there are lines, each containing the name of a guest and an integer denoting how fun the gift from this guest was. Each name only contains English letters, no spaces and is at most characters long. Furthermore, each integer is in the interval to

. No two values are the same.
Output

Print a single line containing the name of the guest that gave Sigrún the most fun gift
"""
n=int(input())
s=0
name=""
for i in range(n):
    line=input().split()
    if int(line[1])>s:
        s=int(line[1])
        name=line[0]
print(name)
