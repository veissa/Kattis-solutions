"""
	Keys, Phone, Wallet
Oh no, you slept in and have to rush to get to work on time! It is also very cold outside!

In your rush to put on Winter gear and leave home quickly, you wonder if you forgot your keys, phone, or wallet. You had better check.
Input

The first line of input contains a single integer
() indicating the number of items you grabbed before heading out the door.
The next lines each contain a single nonempty string of lowercase letters with length at most

indicating an item you grabbed before heading out the door. No two strings will be the same.
Output

Output each of keys, phone, and wallet that does not appear in the input, one per line and in alphabetic order. If you did not forget any of these items, simply print a single line with the text ready
"""




n=int(input())
list=[]
for i in range(n):
    list.append(str(input()))
if ('keys' in list )and ('phone' in list ) and ('wallet' in list):
    print('ready')
nec=['keys','phone','wallet']
for i in nec :
    if i not in list:
        print(i)
