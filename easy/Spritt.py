"""
Everyone at Reykjavík University is disinfecting their hands these days and Elvar isn’t sure if there’s enough sanitizer for all the classrooms. Elvar knows how many bottles of sanitizer are available and how many bottles each classroom needs, but because Elvar is very busy he has a hard time finding out whether there’s enough to go around and asks you to help.
Input

The first line of the input contains two integers n
(), the number of classrooms at Reykjavík University, and x (, how many bottles of sanitizer are available.
 lines, one for each classroom, where the -th line contains one integer (), how many bottles of sanitizer the -th classroom needs. The sum of all will not be over

.
Output

Print Jebb if every classroom can receive the bottles they need and print Neibb otherwise.
""" 
n=input()
a,b = n.split(" ")

s=0
for i in range(int(a)):
    s+=int(input())
    if s> int(b):
        print("Neibb")
        break
print("Jebb")
