

def kysyTiedostonNimi(kehote):
    return input(f"{kehote}: ")

def lue(nimi):
    nopat = []
    heitot = []
    tiedostoAvattu = open(nimi, "r", encoding="UTF-8")

    tiedostoAvattu.readline()

    for rivi in tiedostoAvattu.readlines():
        # Sessio;Hahmo;Noppien määrä;Noppa;Noppien silmäluvu
        riviSplit = rivi.split(";")
        n = riviSplit[3].strip()
        h = len(riviSplit[4].split(","))

        if n in nopat:
            heitot[nopat.index(n)] += h
        else:
            nopat.append(n)
            heitot.append(h)


    tiedostoAvattu.close()

    if('d8' in nopat or 'd20' in nopat):
        heitot[nopat.index('d8')] -= 1
        heitot[nopat.index('d20')] -= 3

    print(f"Tiedosto '{nimi}' luettu.")
    print(f"Analysoitiin {sum(heitot)} nopan heittoa.")
    return nopat, heitot


def kirjoita(nimi, n, h):
    tiedostoAvattu = open(nimi, "w", encoding="UTF-8")


    for i in range(0, len(n)):
        tiedostoAvattu.write(f"Noppaa {n[i]} heitettiin {h[i]} kertaa.\n")


    tiedostoAvattu.close()

    return None









def paaohjelma():

    print("Tämä ohjelma analysoi nopan heittoja.", end="\n")

    luettavanTiedostonNimi = kysyTiedostonNimi("Anna luettavan tiedoston nimi")
    kirjoitettavanTiedostonNimi = kysyTiedostonNimi("Anna kirjoitettavan tiedoston nimi")

    nopat, heitot = lue(luettavanTiedostonNimi)
    kirjoita(kirjoitettavanTiedostonNimi, nopat, heitot)


    print("Kiitos ohjelman käytöstä.", end="\n")


    return None


paaohjelma()