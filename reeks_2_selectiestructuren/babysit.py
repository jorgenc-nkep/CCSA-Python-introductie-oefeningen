uur1 = int(input()) 
min1 = int(input())
uur2 = int(input())  
min2 = int(input()) 

startTijd =uur1*60+min1
eindTijd =uur2*60+min2

GRENS_START=18*60
GRENS_DUURTARIEF=21*60+30 

if eindTijd < startTijd or startTijd < GRENS_START:
    raise "ongeldige invoer"
else:
    goedkoop = max(0, min(eindTijd, GRENS_DUURTARIEF)- startTijd)
    duur = max(0,eindTijd - max(startTijd, GRENS_DUURTARIEF))
    print((goedkoop * 2 + duur * 4)/ 60)