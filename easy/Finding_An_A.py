"""
In this problem, you are given a single string

that is guaranteed to contain the letter a.

You should output the suffix of
that begins with the first occurrence of the letter . Namely, if consists of characters and is the first index with , then you should output the string

.

Why do you want to do this? To solve a problem in the contest!
Input

Input consists of a single line containing a single string
whose length is between and . The string is composed of lowercase letters with no spaces. You are guaranteed the letter a appears at least once in

.
Output

Output the suffix of
that begins with the first occurrence of the letter a.
"""
n=str(input())
print(n[n.find("a"):])
