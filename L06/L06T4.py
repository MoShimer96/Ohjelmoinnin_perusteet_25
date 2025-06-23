


def lue(nimi):
    pieninLuku = 0
    suurinLuku = 0
    pariton = 0
    parillinen = 0
    ensimmainenLuku = True

    luettavaTiedosto = open(nimi, "r", encoding="UTF-8")

    for rivi in luettavaTiedosto.readlines():
        try:
            luku = int(rivi.strip())

            if(luku %2 == 0):
                parillinen += 1
            else:
                pariton += 1

            if(ensimmainenLuku):
                pieninLuku = luku
                suurinLuku = luku
                print(f"Löydettiin uusi pienin luku: {luku}")
                print(f"Löydettiin uusi suurin luku: {luku}")
                ensimmainenLuku = False
            else:
                if(luku < pieninLuku):
                    pieninLuku = luku
                    print(f"Löydettiin uusi pienin luku: {luku}")
                elif(luku > suurinLuku):
                    suurinLuku = luku
                    print(f"Löydettiin uusi suurin luku: {luku}")
        except ValueError:
            continue

    luettavaTiedosto.close()
    print(f"Tiedosto '{nimi}' luettu.", end="\n")
    return  pieninLuku, suurinLuku, parillinen, pariton




def kirjoita(nimi, pienin, suurin, parillisia, parittomia):
    kirjoitettavaTiedosto = open(nimi, "w", encoding="UTF-8")
    kirjoitettavaTiedosto.write(f"Tiedoston pienin luku oli {pienin}.\n")
    kirjoitettavaTiedosto.write(f"Tiedoston suurin luku oli {suurin}.\n")
    kirjoitettavaTiedosto.write(f"Tiedostossa oli {parillisia} parillista ja {parittomia} paritonta lukua.")
    kirjoitettavaTiedosto.close()
    print(f"Tiedosto '{nimi}' kirjoitettu.", end="\n")
    return None

def paaohjelma():

    luettavanTiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    a,b,c,d = lue(luettavanTiedostonNimi)

    kirjoitettavanTiedostonNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    kirjoita(kirjoitettavanTiedostonNimi, a, b, c, d)

    print("Kiitos ohjelman käytöstä.")

    return None


paaohjelma()