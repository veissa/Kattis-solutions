"""
Bartosz and his friends are playing a whispering game at their preschool.

The whispering games plays out with
people sitting in a circle. Some particular person (lets number them ) thinks of a word and whispers it to the person on their left, person . Person then whispers the word to the person on their left, person . This continues until the person to the right of person , let’s number them , has a word whispered to them. At that point person announces out loud what they heard and person

tells everyone what word they thought of in the beginning.

In this preschool all the kids hear the word whispered to them correctly, aside from a single letter, which gets changed.
Input

The first line of the input is the word person
thought of, referred to as the initial word. On the second line is the word that person

heard, referred to as the final word. The initial and final words are the same length. Only English lower case letters are used.
Úttak

One line containing the minimum possible value of

. That is to say, the lowest number of kids that would be needed for the initial word to turn into the final word by playing the whispering game.
Scoring

Group
	

Points
	

Constraints

1
	

10
	

The initial and final words are equal

2
	

20
	

The length of the initial and final words are both

3
	

70
	

The length of the initial and final words are both
Sample Input 1 	Sample Output 1

tommi
dommi

	

2

Sample Input 2 	Sample Output 2

pogger
pepega



"""


one=input()
two=input()
s=1
for i in range(len(one)):
    if one[i]==two[i]:
        s+=0
    else :
        s+=1
print(s)
