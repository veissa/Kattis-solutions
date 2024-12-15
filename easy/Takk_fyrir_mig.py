"""
Little Sigrún is celebrating her birthday today and is expecting a lot of guests. She’s very excited to receive all the packages, but her mother has reminded her to thank people when they give her gifts. Can you help Sigrún in thanking people?
Input

The first line of the input contains an integer
(), the number of guests coming to the party and intending to give Sigrún a gift. Then there are

lines, each containing the name of a guest. Each name only contains English letters and no spaces.
Output

For each guest, print a single line containing Takk name, where name is the name of the guest.
"""
n=int(input())
list=[]
for i in range(n):
    name=str(input())
    list.append(name)
for i in list:
    print("Takk "+i)
