"""
Last night when you went to sleep, you had a strange feeling that you may see the same day again. And your strange feeling came to bewhen you woke up, everyone seemed to think that it was yesterday morning! The same strange feeling came back in the evening.

When this pattern continued for days, you looked for help from a time wizard. The wizard says he can break you out of the time loop, but you must chant his spell. The wizard gives you a magic number, and you must count up to that number, starting at

, saying “Abracadabra” each time.
Input

Input consists of a single integer
(

).
Output

Output the entire wizard’s spell by counting from
to , giving one number and “Abracadabra” per line.
"""
n = int(input())
for i in range(1, n + 1):
    print(f"{i} Abracadabra")
