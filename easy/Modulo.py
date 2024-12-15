"""
Given two integers and , modulo is the remainder when dividing by . For example, the numbers , , and become , , and , modulo . Write a program that accepts numbers as input and outputs the number of distinct numbers in the input, if the numbers are considered modulo

.
Input

The input will contain 10 non-negative integers, each smaller than

, one per line.
Output

Output the number of distinct values when considered modulo

on a single line.
Explanation of Sample Inputs

In sample input
, the numbers modulo are and

.

In sample input
, all numbers modulo are

.

In sample input
, the numbers modulo are and . There are distinct numbers.
"""
holehe=set()
for i in range(10):
    holehe.add(int(input())%42)
print(len(holehe))
