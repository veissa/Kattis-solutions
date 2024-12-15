"""
Once more a low pressure system is over Iceland. Vegagerðin contacts you to ask for help in determining which roads should be closed.

To simplify things we will assume the wind speed is the same over the entire country. You are given the current wind speed, a list of roads and and the maximum safe wind speed for each road.
Input

The first line of the input contains one integer
(), the current wind speed over Iceland. The second line of the input contains one integer (

), the number of roads.

The net
lines will each consist of a string , the name of the road, and an integer (

), which gives the maxiumum safe wind speed for that road, separated by a space.
Output

Print
lines, one for each road, which says whether it is safe to travel that road given the wind speed . Each line should either be “ opin” if it is safe to travel or “ lokud” if it is not to safe to travel along the road

.

Note that the order of the roads should be the same in the input and output.
Scoring

Group
	

Points
	

Constraints

1
	

100
	

No further constraints
Sample Input 1 	

25
2
Oxnadalsheidi 23
Hellisheidi 34


Sample Output 1



Oxnadalsheidi lokud
Hellisheidi opin


"""


current_spead=int(input())
num_roads=int(input())
result=[]
for i in range(num_roads):
    a,b=input().split()
    if current_spead > int(b):
        result.append(a+" lokud")
    else :
        result.append(a+" opin")
for i in result:
    print(i)
