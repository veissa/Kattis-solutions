"""
Per-Magnus managed to solve his addition homework thanks to you, but now he is unfortunately posed with an even greater problem.

He has been given a triangular cake by his mother, and wonders what the area of it is. It turns out Per-Magnus forgot the formula for computing it!

Per-Magnus managed to measure the base and height of the triangle with a ruler. Given this, compute the area of the triangular cake.
Input

The input consists of a single line with two integers
and

, the height and base of the triangle.
Output

Output a single number, the area of the triangle. Your answer must be correct within an absolute or relative error of
.
"""
n,b=input().split()
print(int(n)*int(b)/2)
