print("Tämä ohjelma laskee pizzan hinnan.")

# Pizzan pohjahinta on 9.00 Euroa
hinta = 9.00

onkoPerhe = input("Onko kyseessä perhepizza? (k/e): ").lower()
if(onkoPerhe == "k"):
    hinta *= 1.3
print(f"Pizzan hinta nyt: {hinta:.1f} euroa.\n")

lisataytteetMaara = int(input("Lisätäytteiden määrä: "))
hinta += lisataytteetMaara
print(f"Pizzan hinta nyt: {hinta:.1f} euroa.\n")


kotiinkuljetus = input("Kotiinkuljetus? (k/e): ").lower()
if(kotiinkuljetus == "k"):
    hinta += 4.5
print(f"Pizzan hinta nyt: {f'{hinta:.2f}'.strip('0')} euroa.\n")


kantaasiakas = input("Oletko kanta-asiakas? (k/e): ").lower()
if(kantaasiakas == "k"):
    hinta *= 0.9
print(f"\nPizzan lopullinen hinta valinnoillasi on {f'{hinta:.2f}'.strip('0')} euroa.")

print("Kiitos ohjelman käytöstä.")
