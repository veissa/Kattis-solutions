"""
A common problem in mathematics is to determine which quadrant a given point lies in. There are four quadrants, numbered from to

, as shown in the diagram below:
\includegraphics[width=0.5\textwidth ]{quadrant.png}

For example, the point
, which is at coordinates lies in quadrant since both its and values are positive, and point lies in quadrant 2 since its value is negative and its

value is positive.

Your job is to take a point and determine the quadrant it is in. You can assume that neither of the two coordinates will be

.
Input

The first line of input contains the integer
(). The second line of input contains the integer (

).
Output

Output the quadrant number (
, , or ) for the point .
"""
x=int(input())
y=int(input())
if (x<0 and y<0):
    print("3")
elif (x<0 and y>0):
    print("2")
elif (x>0 and y>0):
    print("1")
else : print("4")
