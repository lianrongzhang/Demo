Id = list(input())
letter = Id[0]
Id.pop(0)
Letter = {'A':10,'B':11,'C':12,'D':13,'E':12,'F':15,'G':16,'H':17,
'I':34,'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,
'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
letter_str = str(Letter[letter])
letter_int = int(letter_str[0]) + (int(letter_str[1])*9)
total = 0
x = 8
for i in Id:
    if(x>0):
        total+=int(i)*x
    else:
        total+=int(i)
    x-=1
if((total+letter_int) % 10==0):
    print("real")
else:
    print('fake')