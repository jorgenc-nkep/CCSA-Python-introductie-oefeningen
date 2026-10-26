from math import sqrt

a = float(input())
b = float(input())
c = float(input())

d =b**2-4*a*c

if d<0 : 
    print("geen wortels")
elif d==0 :
    print(f"1 wortel  /n ${-b/(2*a)}")
else : 
    print("2 wortels")
    w1 = (-b - sqrt(d)) / (2 * a)
    w2 = (-b + sqrt(d)) / (2 * a)
    print(min(w1, w2))
    print(max(w1, w2))