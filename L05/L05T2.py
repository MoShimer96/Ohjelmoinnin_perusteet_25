from itertools import takewhile


def tulostaOhjeet():

    print("Tällä ohjelmalla voit arvata lukua.")
    print("Ohjelma kertoo onko arvauksesi pienempi vai suurempi kuin arvattava luku.\n")
    return None


def kysyLuku(kehote):
    vastaus = int(input(f"{kehote}"))
    return vastaus


def tarkistaLuku(syote, kierros):
    OIKEALUKU =  42

    if(syote == OIKEALUKU):
        kierros += 1
        print("Arvasit oikein! Onneksi olkoon!")
        print(f"Arvasit {kierros} kertaa ennen kuin arvasit oikein.")
        return True, kierros
    else:
        if(OIKEALUKU - syote <= 10 and OIKEALUKU - syote >= -10):
            print("Olet jo lähellä!. Yritä uudelleen.")

        elif(OIKEALUKU - syote < 10):
            print("Luku on paljon pienempi. Yritä uudelleen.")

        elif(OIKEALUKU - syote > -10):
            print("Luku on paljon suurempi. Yritä uudelleen.")
        kierros += 1
        return False, kierros


def paaohjelma():

    tulostaOhjeet()
    arvaukset = 0
    oikein = False

    while(not oikein):
        oikein, arvaukset = tarkistaLuku(kysyLuku("Anna arvauksesi luvusta: "), arvaukset)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()