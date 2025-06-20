alkuarvo = int(input("Anna alkuarvo: "))
loppuarvo = int(input("Kuinka monta seuraavaa tulostetaan: "))

tekstiForSilmukka = ""
tekstiWhileSilmukka = ""

print("\nToteutus for-lauseella:")
for i in range(0, loppuarvo+1):
    tekstiForSilmukka += str(alkuarvo+i) +" "
print(tekstiForSilmukka+"\n", end="\n")

lopetusarvo = loppuarvo + alkuarvo

print("Toteutus while-lauseella:")
while(alkuarvo <= lopetusarvo):
    tekstiWhileSilmukka += str(alkuarvo) + " "
    alkuarvo += 1
print(tekstiWhileSilmukka+"\n")

print("Kiitos ohjelman käytöstä.")