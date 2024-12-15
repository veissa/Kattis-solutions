"""
You have recently begun your job as a civil engineer, or “byggingarverkfræðingur” in Icelandic.

You spend most of your day designing road systems, but since you are in the United States of America, everything is measured in football fields.

You have decided to write a program to convert the measurements from football fields to kilometers.

You may assume
football field is

kilometers.
Input

The first line of the input contains one integer
(

), the length of the road in football fields.
Output

The output should contain a single number on a single line, the length of the road in kilometers. The answer is considered correct if it has an absolute error less than
.
"""
print(f"{float(input())*0.09144:.5f}")
