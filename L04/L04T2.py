import math

print("Tämä ohjelma laskee huvipuiston lipputulot.")

ryhmat = [] # 12 euron lippuhinta
paivaTuotto = 0
keskRyhmakoko = 0


lopeta = False

while(not lopeta):
    valinta = int(input("Anna ryhmän koko väliltä 1-10 henkilöä (0 lopettaa): "))
    if(valinta >= 0 and valinta <= 10):
        if valinta != 0:
            ryhmat.append(valinta)
        else:
            lopeta = True

    else:
        print("Syöte ei ole annetulla välillä, yritä uudestaan.")

for ryhma in ryhmat:
    paivaTuotto += ryhma * 12

print(f"Päivän tuotto oli {paivaTuotto:.1f} euroa.")

keskRyhmakoko =  sum(ryhmat) / len(ryhmat)
print(f"Ryhmän keskimääräinen koko oli {math.ceil(keskRyhmakoko)} henkilöä.")

print("Kiitos ohjelman käytöstä.", end="\n")