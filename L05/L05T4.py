def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna merkkijono")
    print("2) Tulosta merkkijono kasvaen")
    print("3) Tulosta merkkijono pienentyen")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta


def kysyMerkkijono():
    merkkijono = input("Anna merkkijono: ")
    return merkkijono

def tulostaMerkkijonoKasvaen(merkkijono):
    merkkijononPituus = len(merkkijono)
    for i in range(1, merkkijononPituus+1):
        print(merkkijono[0:i])
    return None

def tulostaMerkkijonoPienentyen(merkkijono):
    merkkijononPituus = len(merkkijono)

    while(merkkijononPituus > 0):
        print(merkkijono[:merkkijononPituus])
        merkkijononPituus-=1

    return None


def paaohjelma():
    print("Tällä ohjelmalla voi tulostaa merkkijonoja eri tavoin.")
    merkkijonoPaaohjelma = ""
    lopeta = False

    while(not lopeta):
        valinta = valikko()
        if valinta == 1:
            merkkijonoPaaohjelma = kysyMerkkijono()
            print("")
        elif valinta == 2:
            tulostaMerkkijonoKasvaen(merkkijonoPaaohjelma)
            print("")
        elif valinta == 3:
            tulostaMerkkijonoPienentyen(merkkijonoPaaohjelma)
            print("")
        elif valinta == 0:
            print("Lopetetaan.\n")
            lopeta = True
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print("")

    print("Kiitos ohjelman käytöstä.")

    return None


paaohjelma()