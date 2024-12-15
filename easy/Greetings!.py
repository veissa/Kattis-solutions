"""
Now that Snapchat and Slingshot are soooo 2018, the teenagers of the world have all switched to the new hot app called BAPC (Bidirectional and Private Communication). This app has some stricter social rules than previous iterations. For example, if someone says goodbye using Later!, the other person is expected to reply with Alligator!. You can not keep track of all these social conventions and decide to automate any necessary responses, starting with the most important one: the greetings. When your conversational partner opens with he…ey, you have to respond with hee…eey as well, but using twice as many e’s!
Given a string of the form he…ey of length at most

, print the greeting you will respond with, containing twice as many e’s.
Input

    The input consists of one line containing a single string 

as specified, of length at least and at most

    .

Output

Output the required response
"""



n=str(input()).count('e')
print(n)
print(f"h{2*n*'e'}y")
