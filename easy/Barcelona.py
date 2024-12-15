"""
Arnar, Benni and Unnar were at the airport in Barcelona on their way to a competitive programming training camp. When the plane had landed they exited and went to the baggage claim. When they arrived there was no baggage on the conveyor belts. After a few minutes the baggage started trickling in. When Benni noticed this he loudly proclaimed “My bag’s first! No, it’s second first! No... it’s fourth first. No wait...”

Given a list of bags and a number denoting Benni’s bag, can you help Benni find how first his bag is?
Input

First there is a line with two integers
and , the number of bags and Benni’s bag. It will always hold that and . Next there is a line with integers separated by spaces, . For each it holds that

. No two bags are given by the same number and Benni’s bag always appears in the list.
Output

Print a single line. If Benni’s bag is first print fyrst, if it’s the second print naestfyrst. Otherwise print a single number denoting how first it is followed by the word fyrst after the number
"""
n=input()
l=input()
n=n.split(" ")
l=l.split(" ")
if n[1]==l[0]:
    print("fyrst")
elif n[1]==l[1]:
    print("naestfyrst")
else :
    print(f"{l.index(n[1])+1} fyrst")
