def kysySyote(kehote):
    return input(f"{kehote}")

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Kysy setelin arvo")
    print("2) Lue ja analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    return int(input("Anna valintasi: "))

def analysoi(tiedostonNimi):
    summa = 0
    i = 0
    tiedostoAvattu = open(tiedostonNimi, "r", encoding="UTF-8")
    for line in tiedostoAvattu:
        summa += int(line.strip()) * 1000
        i += 1

    tiedostoAvattu.close()

    print(f"Tiedosto '{tiedostonNimi}' luettu.", end="\n")
    print(f"Analyysi suoritettu, {i} alkiota analysoitu.", end="\n")

    return summa / i

def kirjoita(tiedostonNimi, arvo, maara):
    with open(tiedostonNimi, "w", encoding="UTF-8") as tiedosto:
        tiedosto.write(f"Analysoitiin {arvo} € seteleiden lukumääriä.\n")
        tiedosto.write(f"Keskimäärin seteleitä oli kuukausittain {maara:.0f} kpl.\n")
    print(f"Tiedosto '{tiedostonNimi}' kirjoitettu.")
    tiedosto.close()

    return None

def paaohjelma():
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.")

    setelinArvo = 0
    tulos = 0
    lopeta = False

    while not lopeta:
        valinta = valikko()

        if valinta == 0:
            print("Lopetetaan.\n")
            lopeta = True
        elif valinta == 1:
            setelinArvo = int(input("Anna analysoitavan setelin arvo: "))
            print()
        elif valinta == 2:
            tiedostonNimi = kysySyote("Anna luettavan tiedoston nimi: ")
            tulos = analysoi(tiedostonNimi)
            print()
        elif valinta == 3:
            tiedostonNimi = kysySyote("Anna kirjoitettavan tiedoston nimi: ")
            kirjoita(tiedostonNimi, setelinArvo, tulos)
            print()
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")

    print("Kiitos ohjelman käytöstä.")
    return None
paaohjelma()
