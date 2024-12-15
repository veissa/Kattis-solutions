"""

/problems/fizzbuzz/file/statement/en/img-0001.png
Image by chris morgan cc by
According to Wikipedia, FizzBuzz is a group word game for children to teach them about division. This may or may not be true, but this question is generally used to torture screen young computer science graduates during programming interviews.

Basically, this is how it works: you print the integers from
to , replacing any of them divisible by with Fizz or, if they are divisible by , with Buzz. If the number is divisible by both and

, you print FizzBuzz instead.

Check the samples for further clarification.
Input

Input contains a single test case. Each test case contains three integers on a single line,
, and (

).
Output

Print integers from
to in order, each on its own line, replacing the ones divisible by with Fizz, the ones divisible by with Buzz and ones divisible by both and with FizzBuzz.
Sample Input 1 	
2 3 7

	
Sample Output 1

1
Fizz
Buzz
Fizz
5
FizzBuzz
7




"""





a,b,c=map(int,input().split())
for i in range(1,c+1):
    if (i%a==0) and (i%b==0):
        print("FizzBuzz")
    elif (i%a==0):
        print("Fizz")
    elif (i%b==0):
        print("Buzz")
    else:
        print(i)
