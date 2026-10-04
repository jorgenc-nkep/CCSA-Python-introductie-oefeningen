appels = int(input("Geef het aantal appels in: "))

aantal_kisten = appels//20
aantal_palletten = aantal_kisten // 35
resterend_kisten = aantal_kisten % 35  
resterend_appels = appels%20 

print(f"{aantal_palletten}\n{resterend_kisten}\n{resterend_appels} ")