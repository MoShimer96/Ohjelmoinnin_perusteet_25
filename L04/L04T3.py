print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.")


lopeta = False
setelinArvo = 0
setelienLKM = 0
setelienKokoarvo = 0
while(not lopeta):

    print("Valitse haluamasi toiminto:")
    print("1) Kysy setelin arvo")
    print("2) Kysy setelien lukumäärä")
    print("3) Laske kokonaisarvo")
    print("4) Tulosta tulos")
    print("0) Lopeta")

    valinta = int(input("Anna valintasi: "))

    if(valinta == 1):
        setelinArvo = int(input("Anna analysoitavan setelin arvo: "))
        print("", end="\n")
    elif(valinta == 2):
        setelienLKM = int(input("Anna setelien lukumäärä: "))
        print("", end="\n")
    elif(valinta == 3):
        setelienKokoarvo = setelinArvo * setelienLKM
        print("Setelien kokonaisarvo laskettu.\n")
    elif(valinta == 4):
        print(f"Setelien kokonaisarvo on {setelienKokoarvo} euroa.\n")
    elif(valinta == 0):
        lopeta = True
        print("Lopetetaan.\n")
    else:
        print("Tuntematon valinta,yritä uudestaan.\n")

print("Kiitos ohjelman käytöstä.",end="\n")