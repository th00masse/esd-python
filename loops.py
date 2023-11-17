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


#Somme des Nombres

N = int(input("Entrez un nombre entier N : "))

somme = 0

for i in range(1, N + 1):
    somme += i

print(f"La somme des nombres de 1 à {N} est : {somme}")

#Table de Multiplication

N = int(input("Entrez un nombre entier N : "))
print(f"Table de multiplication de {N} :")
for i in range(1, 11):
    resultat = N * i
    print(f"{N} x {i} = {resultat}")

#Compteur Pair/Impair

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} est un nombre pair.")
    else:
        print(f"{i} est un nombre impair.")


#Factorielle

N = int(input("Entrez un nombre entier N : "))
factorielle = 1

for i in range(1, N + 1):
    factorielle *= i

print(f"La factorielle de {N} est : {factorielle}")
