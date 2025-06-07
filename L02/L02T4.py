merkkijono = input("Anna merkkijono: ")
merkkijononPituus = len(merkkijono)

print("Antamasi merkkijonon pituus oli {} merkkiä.\n".format(merkkijononPituus))

print("Antamasi merkkijonon kaksi ensimmäistä kirjainta ovat {}".format(merkkijono[:2]))
print("Merkkijonon viisi viimeistä kirjainta ovat {}".format(merkkijono[-5:]))
print("Kirjaimet 5, 6, 7, 8 ja 9 ovat {}\n".format(merkkijono[4:9]))
print("Merkkijonon joka toinen kirjain alkaen ensimmäisestä kirjaimesta: {}\n".format(merkkijono[::2]))
print("Antamasi merkkijono '{}' on takaperin '{}'.\n".format(merkkijono, merkkijono[::-1]))

aloituspaikka = int(input("Anna aloituspaikka: "))
lopetuspaikka = int(input("Anna lopetuspaikka: "))
siirtyma = int(input("Anna siirtymä: "))

print("Antamillasi asetuksilla merkkijono {} tulostuu näin: {}\n".format(merkkijono, merkkijono[aloituspaikka:lopetuspaikka:siirtyma]))

print("Kiitos ohjelman käytöstä.")