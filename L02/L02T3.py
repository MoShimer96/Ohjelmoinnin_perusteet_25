print("Tämä ohjelma laskee tuotteen hinnan keskiarvon neljän kaupan hinnoista.")

hinta1 = float(input("Anna hinta ensimmäisessä kaupassa: "))
hinta2 = float(input("Anna hinta toisessa kaupassa: "))
hinta3 = float(input("Anna hinta kolmannessa kaupassa: "))
hinta4 = float(input("Anna hinta viimeisessä kaupassa: "))

summa = hinta1 + hinta2 + hinta3 + hinta4
hintojenKA = summa/4
hintojenKAKokonaisluku = int(hintojenKA)
print("")
print("Antamiesi hintojen summa on {}.".format(summa))
print("Antamiesi hintojen keskiarvo on {0:.1f}.".format(hintojenKA))
print("Keskiarvo on kokonaislukuna {}.".format(hintojenKAKokonaisluku))
print("Kiitos ohjelman käytöstä.")