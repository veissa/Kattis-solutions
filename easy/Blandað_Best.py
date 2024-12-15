"""
Níels is at his favourite kebab place, KFFÍ (Kebab Fyrir Forritara á Íslandi) and now he needs to decide what type of meat he wants on his kebab. KFFÍ offers a wide range of options, a whole two different types, beef or chicken. If you are like Níels, you always prefer getting both mixed together. Níels goes to the counter and asks for special offer number 5, as always, and asks what type of meat they are offering today. Of course, if they offer beef and chicken then he will get them mixed together, otherwise he is content with only taking the one they have, special offer 5 is so good anyway.

Curious as to what Níels got on his kebab, you go to the server and ask him what type of meat they are offering today.
Input

The first line of input contains a positive integer
, the number of meat types KFFÍ is offering today. Next

lines will follow, each one with a unique meat type. The meat type is either "nautakjot" or "kjuklingur".
Output

Output what type of meat Níels got with his offer. If Níels had only "nautakjot" then you should write "nautakjot", if he only got "kjuklingur" then you should write "kjuklingur" and if Níels had both then you should write "blandad best".
"""
n=int(input())
list=[]
for i in range(n):
    list.append(str(input()))
if n<2:
    print(list[0])
else : print("blandad best")
