nimi = input("Kerro nimesi: ")

haalarimerkkienLkm = int(input("Anna haalarimerkkien määrä kokonaislukuna: "))
haalarimerkkienHinta = float(input("Anna haalarimerkkien hinta desimaalilukuna: "))
print("{} annoit lukumääräksi {} ja hinnaksi {}".format(nimi, haalarimerkkienLkm, haalarimerkkienHinta))
haalarimerkkienArvo = haalarimerkkienHinta * haalarimerkkienLkm

print("Haalarimerkkien arvo on tällöin {}".format(haalarimerkkienArvo))

print("Kiitos ohjelman käytöstä.")
