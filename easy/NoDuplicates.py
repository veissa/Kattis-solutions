"""
There is a game in which you try not to repeat a word while your opponent tries to see if you have repeated one.

"THE RAIN IN SPAIN" has no repeats.

"IN THE RAIN AND THE SNOW" repeats THE.

"THE RAIN IN SPAIN IN THE PLAIN" repeats THE and IN.

Write a program to test a phrase.
Input

Input is a line containing words separated by single spaces, where a word consists of one or more uppercase letters. A line contains no more than
characters.
Output

The output is "yes" if no word is repeated, and "no" if one or more words repeat.
"""
def me():
    phrase=str(input()).split()
    for i in phrase :
        if phrase.count(i) >=2:
            return "no"
    return "yes"      
print(me())
