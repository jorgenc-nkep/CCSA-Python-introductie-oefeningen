aantal_stucks = int(input(""))
kostrpijs = float(input(""))
barcodes = int(input(""))
mijlen=int(input(""))
aantal_coupons = aantal_stucks // barcodes

print(f"Phillips spendeerde ${aantal_stucks*kostrpijs} voor {aantal_coupons*mijlen} frequent flyer mijlen.")