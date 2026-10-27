from math import pi 

f1 = 0 
for i in range(1, 101):
    f1 += 1 / i ** 2
print(f1)

doel = pi ** 2 / 6

f2 = 0
n= 0 
while abs(f2 - doel) > 1 / 100: 
    n += 1 
    f2 += 1 / n ** 2
print(n)
