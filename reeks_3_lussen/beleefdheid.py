n = int(input())

beleefdheid = 0

for i in range(1, n):
    som = 0
    getal = i
    while som < n:
        som += getal
        getal += 1
    if som == n:
        beleefdheid += 1

print(beleefdheid)