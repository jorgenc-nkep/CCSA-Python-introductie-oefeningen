def somEchteDelers(n):
    som = 0
    for d in range(1,n):
        if n % d == 0:
            som += d
    return som

a = int(input())
b = int(input()) 

if a != b and somEchteDelers(a) == b and somEchteDelers(b) == a:
    print(f"{a} en {b} zijn bevriende getallen")
else:
    print(f"{a} en {b} zijn niet bevriende getallen")
