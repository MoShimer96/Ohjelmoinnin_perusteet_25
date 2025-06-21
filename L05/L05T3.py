


def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Kysy setelin arvo")
    print("2) Kysy setelien lukumäärä")
    print("3) Laske kokonaisarvo")
    print("4) Tulosta tulos")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta


def kysyLuku(kehote):
    luku = int(input(f"{kehote}"))
    return luku
def analysoi(a,b):
    return a*b


def tulostaTulokset(parametri):
    print(f"Setelien kokonaisarvo on {parametri} euroa.")
    return None



def paaohjelma():
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.")
    setelinArvo = 0
    setelienLKM = 0
    setelienKokoarvo = 0


    while(True):
        valinta = valikko()
        if(valinta == 1):
            setelinArvo = kysyLuku("Anna analysoitavan setelin arvo: ")
            print("")
            continue
        elif(valinta == 2):
            setelienLKM = kysyLuku("Anna setelien lukumäärä: ")
            print("")
            continue
        elif(valinta == 3):
            setelienKokoarvo = analysoi(setelinArvo, setelienLKM)
            print("Setelien kokonaisarvo laskettu.\n")

            continue
        elif(valinta == 4):
            tulostaTulokset(setelienKokoarvo)
            print("")
            continue
        elif(valinta == 0):
            print("Lopetetaan.\n")
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print("")
            continue

    return None

paaohjelma()