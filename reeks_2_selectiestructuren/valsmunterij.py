weging1 = input("Geef de resultaten van de 1ste weging: ")
weging2 = input("Geef de resultaten van de 2de weging: ")

if weging1 == "links":
    start = 1
elif weging1 == "rechts":
    start = 4
else:
    start = 7

if weging2 == "links":
    n = start
elif weging2 == "rechts":
    n = start + 1
else:
    n = start + 2

print(f"muntstuk #{n} is vervalst")