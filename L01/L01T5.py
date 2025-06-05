pakettienLkm = int(input("Anna pakettien lukumäärä: ")) 
PaketinPaino = int(input("Anna yhden paketin paino kokonaisina kilogrammoina: "))
paino = pakettienLkm * PaketinPaino
print("Paketteja on {} ja yksi paketti painaa {} kilogrammaa.".format(pakettienLkm, PaketinPaino))
print("Yhteensä paketit painavat {} kilogrammaa.".format(paino))