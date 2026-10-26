verslaat = {
    "schaar": ["blad", "hagedis"],
    "blad": ["steen", "spock"],
    "steen": ["hagedis", "schaar"],
    "hagedis": ["spock", "blad"],
    "spock": ["schaar", "steen"],
}

speler1 = input()
speler2 = input()
if speler1 not in verslaat or speler2 not in verslaat:
    raise "foutieve invoer !!!"
if speler1 == speler2:
    print("gelijkspel")
elif speler2 in verslaat[speler1]:
    print("speler1 wint")
else:
    print("speler2 wint")