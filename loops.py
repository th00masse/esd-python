def multiplie(a, b):
    valeur = 0

    for i in range(b):
        valeur1 += a

    return resultat
#1

x = int(input("Saisissez une première valeur: "))
y = int(input("Saisissez une seconde valeur: "))
produit = multiplie(x, y)
print("Le résultat de la multiplication est :", x, "*", y, "=", produit)




# 2

def puissance(base, exposant):
    valeur2 = 1

    for _ in range(exposant):
        valeur2 *= base

    return valeur2

base = int(input("Entrez la base "))
exposant = int(input("Entrez l'exposant "))
valeur2 = puissance(base, exposant)
print("Le résultat est :", base, "^", exposant, "=", resultat)
