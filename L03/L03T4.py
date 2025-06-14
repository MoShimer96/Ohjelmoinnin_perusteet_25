print("Selvitetään tuotteen hintaluokka.")

hinta = float(input("Anna tuotteen hinta: "))

print("Selvitetäänkö luokka")
print("1) yhdellä monihaaraisella valintarakenteella")
print("2) useilla erillisillä valintarakenteilla?")
valinta = int(input("Anna valintasi: "))
Tuloste = None
if(valinta == 1):
    print(f"\nAnnoit tuotteen hinnaksi {hinta} euroa.")
    if(hinta < 5):
        Tuloste = "Tuotteen hintaluokka on tällöin A."
    elif(hinta < 10):
        Tuloste = "Tuotteen hintaluokka on tällöin B."
    elif(hinta < 25):
        Tuloste = "Tuotteen hintaluokka on tällöin C."
    elif(hinta < 50):
        Tuloste = "Tuotteen hintaluokka on tällöin D."
    else:
        Tuloste = "Tuotteen hintaluokka on tällöin E."
if(valinta == 2):
    print(f"\nAnnoit tuotteen hinnaksi {hinta} euroa.")
    if(hinta < 5):
        Tuloste = "Tuotteen hintaluokka on tällöin A."
    if(hinta < 10):
        Tuloste = "Tuotteen hintaluokka on tällöin B."
    if(hinta < 25):
        Tuloste = "Tuotteen hintaluokka on tällöin C."
    if(hinta < 50):
        Tuloste = "Tuotteen hintaluokka on tällöin D."
    if(hinta >= 50):
        Tuloste = "Tuotteen hintaluokka on tällöin E."

print(Tuloste)
print("Kiitos ohjelman käytöstä.")