"""
A known problem with some microphones is the “hissing s”. That is, sometimes the sound of the letter s is particularly pronounced; it stands out from the rest of the word in an unpleasant way.

Of particular annoyance are words that contain the letter s twice in a row. Words like amiss, kiss, mississippi and even hiss itself.
Input

The input contains a single string on a single line. This string consists of only lowercase letters (no spaces) and has between
and characters.
Output

Output a single line. If the input string contains two consecutive occurrences of the letter s, then output hiss. Otherwise, output no hiss.
"""
word=str(input())
if "ss" in word:
    print("hiss")
else :
    print("no hiss")
