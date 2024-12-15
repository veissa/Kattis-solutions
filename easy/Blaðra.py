"""
The common element of birthdays and programming contests are the balloons. You have arrived to the 20 year anniversary of Forritunarkeppni Framhaldsskólanna. There you receive a really neat balloon.

OH NO!

You lose your grip on the balloon and it floats upwards. If you find a long stick or a ladder you might be able to reach it and pull it back down.

The balloon was moving when you lost your grip, so it has an initial velocity
. Its acceleration is and you estimate it will take you seconds to get the equipment to save the balloon. Now you just need to find the distance that the balloon has traveled. Luckily you learned at school that
. What’s the value of

?
Input

The input is one line and consists of three integers
, the initial velocity of the balloon, , the acceleration of the balloon and

, the duration of time for which the balloon travels.
Output

Print a single line containing the value
. The answer is considered correct if its absolute or relative error from the correct answer is at most . This means it does not matter how many significant digits the answer contains as long as its accurate enough.
"""
n = input().split()

v0 = float(n[0])
a = float(n[1])
t = float(n[2])

d = v0 * t + 0.5 * a * (t ** 2)

print(f"{d:.5f}")
