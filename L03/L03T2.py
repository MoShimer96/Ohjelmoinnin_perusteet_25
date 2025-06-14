print("Selvitetään sanojen aakkosjärjestys.")
sana1 = input("Anna sana 1: ")
sana2 = input("Anna sana 2: ")

def akkosjarjestys(a, b):
    if(a > b):
        print(f"'{b}' on aakkosissa aiemmin kuin '{a}'.")
    else:
        print(f"'{a}' on aakkosissa aiemmin kuin '{b}'.")
    return None

akkosjarjestys(sana1, sana2)

print("")
print("Selvitetään merkin sisältyminen merkkijonoon.")

merkki = input("Anna etsittävä merkki: ")

def onkoMerkkiMerkkijonossa(merkki, merkkijono):
    if(merkki in merkkijono):
        print(f"Merkki '{merkki}' sisältyy merkkijonoon '{merkkijono}'.")
    else:
        print(f"Merkki '{merkki}' ei sisälly merkkijonoon '{merkkijono}'.")
    
    return None

onkoMerkkiMerkkijonossa(merkki, sana1)
onkoMerkkiMerkkijonossa(merkki, sana2)
print("")

print("Selvitetään, onko sana palindromi.")
pallindromi = input("Anna testattava sana: ")

def onkoPalindromi(merkkijono):
    if(merkkijono == merkkijono[::-1]):
        print(f"Sana '{merkkijono}' on palindromi.")
    else:
        print("Sana ei ole palindromi.")
        print(f"Sana on etuperin '{merkkijono}' ja takaperin '{merkkijono[::-1]}'.")

    return None
onkoPalindromi(pallindromi)
print("Kiitos ohjelman käytöstä.")