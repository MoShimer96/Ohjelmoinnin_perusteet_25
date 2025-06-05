Luku1 = 456
Luku2 = 789

Erotus = Luku2 - Luku1
Summa = Luku1 + Luku2
Tulos = Summa * Erotus
JakojaannoLuku1 = Luku1 % 2 
JakojaannoLuku2 = Luku2 % 2

print("{} - {} = {}".format(Luku2, Luku1, Erotus))
print("{} + {} = {}".format(Luku1, Luku2, Summa))
print("{} * {} = {}".format(Summa, Erotus, Tulos))

print("( {} - {} ) * ( {} + {} ) = {}".format(Luku2, Luku1, Luku1, Luku2, Tulos))

print("Luvun {} jakojäännös 2 :lla on {}".format(Luku1, JakojaannoLuku1))
print("Luvun {} jakojäännös 2 :lla on {}".format(Luku2, JakojaannoLuku2))

