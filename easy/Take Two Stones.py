"""
Alice and Bob are playing a new game of stones. There are stones placed on the ground, forming a sequence. The stones are labeled from to

.

Alice and Bob in turns take exactly two consecutive stones on the ground until there are no consecutive stones on the ground. That is, each player can take stone
and stone , where

. If the number of stone left is odd, Alice wins. Otherwise, Bob wins.

Assume both Alice and Bob play optimally and Alice plays first, do you know who the winner is?
Input

The input contains an integer

, the number of stones.
Output

Output the winner, “Alice” or “Bob” (without the quotes), on a line.
"""
N=int(input())
if (N%2)%2==0:
    print("Bob")
else : print("Alice")
