"""In a recent data leak, some of the things the CIA has been examining were revealed. One of the items that came to light was that they had a tool, which could find email addresses that have been obscured by adding spaces, in order to avoid spam. The Icelandic Intelligence Agency has requested that the Competitive Programming Association of Iceland makes contestants implement a similar tool.
Input

Input is a single line with one email address, which consists exclusively of lowercase letters in the English alphabet, spaces, full stops and exactly one @ symbol. The line will always start with a lowercase letter and end with a lowercase letter or a full stop.
Output

Output the email address, without any spaces, on a single line.
"""
print("".join(str(input()).split()))
