def tiedostoLue(tiedostonNimi):

    i = 0
    summa = 0
    keskiarvo = 0
    tiedostoAvattu = open(tiedostonNimi, "r", encoding="UTF-8")

    for line in tiedostoAvattu.readlines():
        summa += float(line.strip())
        i+=1
    keskiarvo = summa / i
    print(f"Tiedostossa '{tiedostonNimi}' oli {i} lukua.", end="\n")
    print(f"Lukujen keskiarvo oli {keskiarvo:.2f} ja summa {summa}.", end="\n")
    print("Kiitos ohjelman käytöstä.", end="\n")

    tiedostoAvattu.close()

    return None



def paaohjelma():
    syote = input("Anna luettavan tiedoston nimi: ")
    tiedostoLue(syote)
    return None

paaohjelma()