"""
Reduplication is when one repeats a word several times, often to reinforce or alter its meaning. In some languages, such as Indonesian, reduplication is very common and serves various grammatical functions. Even in Swedish, reduplication is used occasionally, for example, saying "hej hej" instead of just "hej".

Rama is a diligent user of reduplication when chatting with his friends. He sometimes writes the same word up to nine times, which takes a long time. Therefore, he usually writes the word once, followed by a number indicating how many times the word should be repeated.

Write a program that reads in a word Rama intends to repeat and how many times it should be repeated. The program should then print the word repeated the correct number of times.
Input

The first line of the input contains a string
(

), the word Rama wants to write. The word consists of letters from a-z.

The next line contains a digit between
and

, the number of times Rama wants to write the word.
Output

Print
as many times as the digit indicates.
"""
txt=str(input())
rep=int(input())
print(rep*txt)
