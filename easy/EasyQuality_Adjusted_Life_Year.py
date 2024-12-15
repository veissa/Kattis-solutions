"""
The Quality-Adjusted Life-Year (QALY) is a way to measure a person’s quality of life that includes both the quality and the quantity of life lived.

The quality of life lived can be quantified as a number between
and . If someone is living with perfect health, the quality of life is . If someone is dead, then the quality of life is

. The quality of life may increase or decrease due to medical treatements, sickness, etc.

The QALY for each period in which the quality of life is constant is simply the product of the quality of life and the length of the period (in years). We wish to know the amount of QALY accumulated by a person at the time of death, given the complete history of this person.
Input

The first line of input contains a single integer
 (

), which is the number of periods of constant quality of life during the person’s lifetime.

The next
lines describe the periods of life. Each of these lines contains two real numbers  (), which is the quality of life in this period, and  (

), which is the number of years in this period. All real numbers will be specified to exactly one decimal place.
Output

Display the QALY accumulated by the person. Your answer will be considered correct if its absolute error does not exceed
.
"""
N=int(input())
s=0
for i in range(N):
    a=input().split()
    s+=float(a[0])*float(a[1])
print(f"{s:.3f}")
