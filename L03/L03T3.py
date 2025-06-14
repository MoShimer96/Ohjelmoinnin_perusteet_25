print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")

     
 
 

print("Valitse haluamasi toiminto:") 
print("1) Tulosta merkkijonon ensimmäinen puolikas") 
print("2) Tulosta merkkijonon toinen puolikas") 
print("3) Tulosta merkkijonon pituus") 
print("0) Lopeta") 
Valinta = int(input("Anna valintasi: ")) 
if (Valinta == 1): 
    Merkkijono = input("Anna merkkijono: ")
    pituus = len(Merkkijono)
    print(f"Merkkijonon ensimmäinen puolikas on '{Merkkijono[:int(pituus/2)]}'.")
elif (Valinta == 2):
    Merkkijono = input("Anna merkkijono: ")
    pituus = len(Merkkijono)
    print(f"Merkkijono toinen puolikas on '{Merkkijono[int(pituus/2):]}'.")
elif (Valinta == 3): 
    Merkkijono = input("Anna merkkijono: ")
    print(f"Merkkijonon pituus on {len(Merkkijono)}.") 
elif (Valinta == 0): 
    Merkkijono = input("Anna merkkijono: ")
    print("Lopetetaan.") 
else: 
    Merkkijono = input("Anna merkkijono: ")
    print("Tuntematon valinta.") 
    


print("Kiitos ohjelman käytöstä.")