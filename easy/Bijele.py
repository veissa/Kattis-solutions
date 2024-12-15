
"""
Mirko has found an old chessboard and a set of pieces in his attic. Unfortunately, the set contains only white pieces, and apparently an incorrect number of them. A set of pieces should contain:

    One king

    One queen

    Two rooks

    Two bishops

    Two knights

    Eight pawns

Mirko would like to know how many pieces of each type he should add or remove to make a valid set.
Input

The input consists of
integers on a single line, each between and

(inclusive). The numbers are, in order, the numbers of kings, queens, rooks, bishops, knights and pawns in the set Mirko found.
Output

Output should consist of
integers on a single line; the number of pieces of each type Mirko should add or remove. If a number is positive, Mirko needs to add that many pieces. If a number is negative, Mirko needs to remove pieces.
"""










pieces=input()
pieces=pieces.split(" ")
a=int(pieces[0])
if a>1:
    remove=a-1
    print(-remove,end=" ")
elif a==1:
    print(0,end=" ")
else :
    print(1,end=" ")
b=int(pieces[1])
if b>1:
    remove=b-1
    print(-remove,end=" ")
elif b==1:
    print(0,end=" ")
else :
    print(1,end=" ")
c=int(pieces[2])
if c>2:
    remove=c-2
    print(-remove,end=" ")
elif c==2:
    print(0,end=" ")
else :
    add=2-c
    print(add,end=" ")
d=int(pieces[3])
if d>2:
    remove=d-2
    print(-remove,end=" ")
elif d==2:
    print(0,end=" ")
else :
    add=2-d
    print(add,end=" ")
e=int(pieces[4])
if e>2:
    remove=e-2
    print(-remove,end=" ")
elif e ==2:
    print(0,end=" ")
else :
    add=2-e
    print(add,end=" ")
f=int(pieces[5])
if f>8:
    remove=f-8
    print(-remove,end=" ")
elif f==8:
    print(0,end=" ")
else :
    add=8-f
    print(add,end=" ")



