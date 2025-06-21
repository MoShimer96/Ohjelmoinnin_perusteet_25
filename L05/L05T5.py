def laskeJakso(luku):
    lukuLista =[luku]

    while luku != 1:
        if luku % 2 == 0:
             luku = int(luku/2)
        else:
            luku = int(3*luku+1)
        lukuLista.append(luku)
    return len(lukuLista)


def kysyLuku(kehote):
    palaute = int(input(f"{kehote}"))
    return palaute

def etsiPisin(a,b):
    pisin = a
    pituus = 0

    for i in range(a,b):
        jaksonPituus = laskeJakso(i)
        if jaksonPituus > pituus:
            pisin = i
            pituus = jaksonPituus
    print(f"Suurin Collatz-jakso oli luvulla {pisin}.")
    print(f"Jakson pituus oli {pituus} termiä.")

    return None


def paaohjelma():
    print("Tämä ohjelma etsii pisimmän Collatz-jakson annetulla välillä.")
    alku = kysyLuku("Anna lukualueen alku: ")
    loppu = kysyLuku("Anna lukualueen loppu: ")
    etsiPisin(alku, loppu)
    print("Kiitos ohjelman käytöstä.", end="\n")
    return None

paaohjelma()