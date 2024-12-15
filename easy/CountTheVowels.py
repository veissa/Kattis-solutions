"""
Given a line of text, count the vowels! For this problem, the only vowels are A, E, I, O and U, both upper and lower case. No other letters will be considered vowels for the purposes of this problem.
Input

The single line of input contains a single string
(), which consists of ASCII text, with no special characters. There will be only letters, numbers, printable symbols, and spaces. There will be no control characters, and the only white space will be the space character. The string

is guaranteed to have at least one non-whitespace character
Output

Output a single line with a single integer, which is the number of vowels in
.
"""
n=str(input())
vowels={'a','A','e','E','o','O','I','i','U','u'}
print(sum(1 for i in n if i in vowels))
