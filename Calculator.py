def calcul_litteral(x, y, z):
    # Calculs littéraux
    resultat1 = 2 * x + 11
    resultat2 = (2 * z + y) - 5
    resultat3 = (y + z) - x

    # Retour des résultats dans l'ordre des calculs
    return resultat1, resultat2, resultat3

# Exemple d'utilisation
# Saisir les valeurs de x, y et z
x = int(input("Entrez la valeur de x : "))
y = int(input("Entrez la valeur de y : "))
z = int(input("Entrez la valeur de z : "))

# Appel de la fonction et affichage des résultats
resultat1, resultat2, resultat3 = calcul_litteral(x, y, z)
print(f"Résultat du premier calcul (2x + 11) : {resultat1}")
print(f"Résultat du deuxième calcul ((2Z + y) - 5) : {resultat2}")
print(f"Résultat du troisième calcul ((y + Z) - x) : {resultat3}")
input("Appuyez sur Entrée pour quitter...")
