"""
In this problem, your program should read two whole numbers (also called integers) from the input, and print them out in increasing order.

As a refresher, here are some ways to read two numbers from standard input in a few different languages:

# Python 3
line = input()
a, b = line.split()
a = int(a)
b = int(b)

// C++
// make sure to first "#include <iostream>"
int a, b;
std::cin >> a >> b;

// Java
// make sure to first "import java.util.Scanner;"
Scanner s = new Scanner(System.in);
int a = s.nextInt(), b = s.nextInt();

Input

The input contains one line, which has two integers
and , separated by a single space. The bounds on these values are

.
Output

Output the smaller number first, and the larger number second.
"""
a,b =input().split()
if int(a)<int(b):
    print(a,end=" ")
    print(b)
else :
    print(b,end=" ")
    print(a)
