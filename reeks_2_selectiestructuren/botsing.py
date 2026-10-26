x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input()) 
x3 = int(input()) 
y3 = int(input())
x4 = int(input())
y4 = int(input()) 

a_links, a_rechts = min(x1, x2), max(x1, x2)
a_onder, a_boven = min(y1, y2), max(y1, y2) 

b_links, b_rechts = min(x3, x4),max(x3, x4)
b_onder, b_boven = min(y3, y4), max(y3, y4) 

if a_links <b_rechts and b_links< a_rechts and a_onder < b_boven and b_onder < a_boven :
    print("botsing") 
else:
    print("geen botsing")