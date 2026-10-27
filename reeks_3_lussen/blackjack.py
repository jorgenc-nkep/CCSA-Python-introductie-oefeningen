# tot = 0 
# kaart=int(input)

# while kaart != 0 and tot+kaart <21 : 
#     tot += kaart
#     kaart = int(input())

# tot += kaart

# if tot == 21:
#     print("Gewonnen!")
# elif tot > 21:
#     print(f"Verbrand ({tot})")
# else:
#     print(f"Voorzichtig gespeeld ({tot})")


## speelbare blackjack (leuker)

import random 

tot = 0 
keuze = ""
kaart = 0

while keuze != "stop" and tot < 21:
    kaart = random.randint(1, 11)
    tot += kaart 
    print(f"Je trok {kaart} (tot: {tot})")
    if tot < 21 :
        keuze = input("Schrijf stop als je niet meer voort wilt: ").strip().lower()



if tot == 21 :
    print("Gewonnen!")
elif tot > 21 : 
    print(f"Verbrand ({tot})")
else: 
    print(f"Voorzichtig gespeeld ({tot})")
