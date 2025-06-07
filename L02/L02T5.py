print("Tämä ohjelma laskee pituuksien yksikkömuunnoksia.")
pituusTuumina = float(input("Anna pituus tuumina: "))
pituusTuuminaSM = pituusTuumina * 25.40 * 0.1
print(f"Pituus on {pituusTuumina} tuumaa eli {pituusTuuminaSM:.1f} senttimetriä.")

pituusMaileina = float(input("Anna pituus maileina: "))
pituusMaileinaKM = pituusMaileina * 1.609344
print(f"Pituus on {pituusMaileina} mailia eli {pituusMaileinaKM:.2f} kilometriä.")

print("Kiitos ohjelman käytöstä.")