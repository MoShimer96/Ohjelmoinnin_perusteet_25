

def tiedostoKirjoita( kirjoitettavanTiedostonNimi ):

    tiedosto =  open(kirjoitettavanTiedostonNimi, "w", encoding="UTF-8")

    while(True):
        syote = input("Anna tiedostoon tallennettava desimaaliluku (enter lopettaa): ")
        if (syote == ""):
            break
        else:
            tiedosto.write(syote+"\n")

    tiedosto.close()

    print(f"Tiedosto '{kirjoitettavanTiedostonNimi}' kirjoitettu.", end="\n")
    return None


def paaohjelma():
    syoteTiedostonNimi = input("Anna tallennettavan tiedoston nimi: ")
    tiedostoKirjoita(syoteTiedostonNimi)
    print("Kiitos ohjelman käytöstä.", end="\n")
    return None

paaohjelma()