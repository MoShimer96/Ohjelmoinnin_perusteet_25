def tulostaOhjeet():
    print("Tämä aliohjelma tulostaa ohjeita käyttäjälle.")
    print("Anna ensin kaksi lukua.")
    return None

def kysyLuku(kehote):
    print("Tämä aliohjelma kysyy luvun.")
    luku = int(input(f"{kehote}"))

    return luku

def tulostaTulokset(a, b):
    print("Tämä aliohjelma tulostaa luvut ja niiden parillisuuden.")
    if(a%2 == 0):
        print(f"{a} on parillinen luku.")
    else:
        print(f"{a} ei ole parillinen luku.")

    if(b%2 == 0):
        print(f"{b} on parillinen luku.")
    else:
        print(f"{b} ei ole parillinen luku.")

    return None

def paaohjelma():
    print("Tämä ohjelma kysyy ja tulostaa tietoja.")
    tulostaOhjeet()
    luku1 = kysyLuku("Anna ensimmäinen luku: ")
    luku2 = kysyLuku("Anna toinen luku: ")
    tulostaTulokset(luku1, luku2)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
