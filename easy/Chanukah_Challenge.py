"""
The Jewish holiday of Chanukah lasts for eight days and eight nights. On the evening before each day, candles are lit in a menorah. On the first evening, one candle is lit, on the second, two are lit, and so on. However, each evening, an extra candle, called the shammas, is also lit (in fact, this candle is used to light the other candles). Thus, for the entire holiday,

candles are necessary.

But what if Chanukah lasted a different number of days? How many candles would be needed?

For this problem, you will write a program that determines how many candles would be necessary for a Chanukah holiday lasting for a given number of days.
Input

The first line of input contains a single decimal integer
, (

), which is the number of data sets that follow. Each data set should be processed identically and independently.

Each data set consists of a single line of input. It contains the data set number,
, followed by a single space, followed by a single decimal integer , (), which gives the number of days to assume for the holiday. The data set number starts at and is incremented by for each data set.
"""
n=int(input())
final=[]
for i in range(n):
    data=input().split()
    s=2*int(data[1])
    for j in range(int(data[1])):
        s+=j
    final.append(s)
for i in range(1,n+1):
    print(f"{i} ",final[i-1])
