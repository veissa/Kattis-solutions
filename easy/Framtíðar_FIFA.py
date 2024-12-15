"""
 You: Where am I? you say, equal parts awake and asleep
You approach a muffled cheer coming from another room, a sound not unlike that of a goal being celebrated
You: Who are you? What year is it?
A strangely dressed man rises to his feet
Stranger 1: Ahh, I see you’ve awaken. I didn’t expect it so soon. The FreezeChamber 9000 must be on the fritz.
You notice a second man lounging on a sofa, playing FIFA
Stranger 2: Lalli! Sit down! The game isn’t over yet.
Lalli: Okay, sorry. Hey, we’ll conclude this discussion when I finish this game. You watch intently and can’t help but notice the disheartening lack of improvements to the video game during your slumber.
You: Has FIFA not changed at all since I entered the FreezeChamber 9000?
Lalli: Sure it has. There have been

    improvements since you froze.
    Stranger 2: Lalli! Focus! 

Since you know the FIFA games only receive

improvements every year, and you know you entered the FreezeChamber 9000 in the year 2022, you can determine what year it is.
Input

The input consists of two lines. The first line contains an integer
(), the number of improvements since you were frozen. The second line contains an integer (

), the number of improvements the game receives every year. Every year there is one new version of the game released and it’s released on the first day of the year.
Output

Print the current year.
"""
impros=int(input())
every=int(input())
print(2022 + (impros // every))
