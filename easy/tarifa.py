"""
Pero has negotiated a Very Good data plan with his internet provider. The provider will let Pero use up

megabytes to surf the internet per month. Each megabyte that he doesn’t spend in that month gets transferred to the next month and can still be spent. Of course, Pero can only spend the megabytes he actually has.

If we know how much megabytes Pero has spent in each of the first
months of using the plan, determine how many megabytes Pero will have available in the

month of using the plan.
Input

The first line of input contains the integer
(). The second line of input contains the integer (). Each of the following lines contains an integer (), the number of megabytes spent in each of the first months of using the plan. Numbers

will be such that Pero will never use more megabytes than he actually has.
Output

The first and only line of output must contain the required value from the task.
Sample Input 1 	

10
3
4
6
2

Sample Output 1

28

"""


x=int(input())
N=int(input())
Res=x
for i in range(N):
    Res+=(x-int(input()))
print(Res)
