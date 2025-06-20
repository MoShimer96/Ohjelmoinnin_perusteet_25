print("Tämä ohjelma tarkistaa käyttäjätunnuksen oikeellisuuden.", end="\n")

minimipituus = int(input("Anna tunnuksen minimipituus: "))
ensimmainenMerkki = input("Anna tunnuksen ensimmäinen merkki: ")
tunnus = ""
print("", end="\n")
while True:

    tunnus = input("Anna tarkistettava tunnus: ")

    if len(tunnus) < minimipituus:
        print("Tunnus ei ole riittävän pitkä, yritä uudelleen.", end="\n")
    elif "!" in tunnus or ";" in tunnus or " " in tunnus:
        print("Tunnus ei saa sisältää välilyöntiä tai merkkejä '!' ja ';', yritä uudelleen.")
    elif tunnus[0] != ensimmainenMerkki:
        print(f"Tunnuksen ensimmäinen merkki ei ole '{ensimmainenMerkki}', yritä uudelleen.",end="\n")

    else:
        print("Tunnus täyttää ehdot, lopetetaan.", end="\n")
        break

print("Kiitos ohjelman käytöstä.", end="\n")