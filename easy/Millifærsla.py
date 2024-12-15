""" 
Bjarki forgot his wallet when he went out to eat with Hlynur. Hlynur paid for him and told Bjarki that he could use the service Monnei to pay it back. Bjarki thought Monnei had the highest transaction fee, higher than the other services Fjee and Dolladollabilljoll. He told Hlynur that he would transfer the money using the service with the lowest transaction fee. He needs your help to determine the correct service though.
Input

The input consists of three lines. The first line consists of a single integer
, the transaction fee on Monnei. The second line consists of a single integer , the transaction fee on Fjee. The third line consists of a single integer

, the transaction fee on Dolladollabilljoll.
Output

Output the name of the service with the lowest transaction fee in a single line
."""
a=int(input())
b=int(input())
c=int(input())
le=min(a,b,c)
if le==a: print("Monnei")
elif le==b: print("Fjee")
else : print("Dolladollabilljoll")
