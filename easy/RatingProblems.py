"""
Your judges are preparing a problem set, and they’re trying to evaluate a problem for inclusion in the set. Each judge rates the problem with an integer between and

, where:

means: I really like this problem!

means: I really don’t like this problem!

means: Meh. I don’t care if we use this problem or not.
The overall rating of the problem is the average of all of the judges’ ratings—that is, the sum of the ratings divided by the number of judges providing a rating.

Some judges have already rated the problem. Compute the minimum and maximum possible overall rating that the problem can end up with after the other judges submit their ratings.
Input
The first line of input contains two integers () and (), where is the total number of judges, and

is the number of judges who have already rated the problem.

Each of the next
lines contains a single integer (). These are the ratings of the

judges that have already rated the problem.
Output

Output two space-separated floating point numbers on a single line, which are the minimum and maximum overall rating the problem could achieve after the remaining judges rate the problem, minimum first. These values must be accurate to an absolute or relative error of
.
"""




judges,default=input().split()
s=0
for i in range(int(default)):
    s+=int(input())
mini=((int(default)-int(judges))*3 + s)/int(judges)
maxi=((int(judges)-int(default))*3 + s)/int(judges)
print(f"{mini} {maxi}")
