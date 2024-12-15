"""

/problems/hipphipphurra/file/statement/en/img-0001.jpg
Image from flickr.com
It’s not just Forritunarkeppni Framhaldsskólanna that’s celebrating their anniversary this year. Shouldn’t we congratulate the others as well?
Input

The first line contains the name of a person celebrating their birthday, the name only contains English letters and no whitespace. The second line contains a single integer, how old they are now.
Output

If the person is now
years old, print lines. Each line should contain Hipp hipp hurra, name!, where name is the person’s name.
"""
name=str(input())
age=int(input())
for i in range(age):
    print("Hipp hipp hurra, "+name+"!")
