print("Anna kaksi kokonaislukua.")

luku1 = int(input("Anna luku 1: "))
luku2 = int(input("Anna luku 2: "))
print("Selvitetään, ovatko antamasi luvut parillisia.")

def onkoParillinen(luku):
    
    if(luku%2 == 0):
        print(f"Luku {luku} on parillinen.")
    else:
        print(f"Luku {luku} on pariton.")
    
    return None

def kumpiOnSuurempi(a, b):
    print("Selvitetään, kumpi antamistasi luvuista on suurempi.")
    if(a == b):
        print(f"Luvut {a} ja {b} ovat yhtä suuria.")
    elif(a > b):
        print(f"Luku {a} on suurempi.")
    else:
        print(f"Luku {b} on suurempi.")
    return None

onkoParillinen(luku1)
onkoParillinen(luku2)
kumpiOnSuurempi(luku1, luku2)


print("Kiitos ohjelman käytöstä.")