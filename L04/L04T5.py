print("Tämä ohjelma laskee Collatz-sarjoja.")


alkuarvo = int(input("Anna alkuarvo: "))

arvot = [alkuarvo]
print(f"Luvun {alkuarvo} Collatz-jakso on:")
while alkuarvo != 1:
    if alkuarvo%2 == 0:
        alkuarvo = alkuarvo // 2
    else:
        alkuarvo = 3*alkuarvo +1
    arvot.append(alkuarvo)

print(" -> ".join(str(luku) for luku in arvot))
print(f"Luvun {arvot[0]} Collatz-jaksossa on {len(arvot)} termiä.")
print("Kiitos ohjelman käytöstä.", end="\n")