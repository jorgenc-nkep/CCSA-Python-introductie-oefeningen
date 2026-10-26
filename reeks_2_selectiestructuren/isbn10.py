cijfers = []
for i in range(10):
    cijfers.append(int(input()))

som = 0 

print(len(cijfers))

for i in range(len(cijfers)-1):
    som += (i + 1)  * cijfers[i]

controlecijfer = som % 11

if controlecijfer == cijfers[9]:
    print("OK")
else:
    print("FOUT")