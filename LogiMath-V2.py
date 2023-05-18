# -*- coding: utf-8 -*-
import math

print("Programme développé par LogiCorp")
print("")
print("LogiMath AEO V4.5")
print("")

print("")
print("Bonjour et bienvenue sur la calculatrice LogiCorp,")
print("")
print("Nous vous invitons à entrer un nombre pour les variables a et b.")
print("")
print("Avant de commencer, veuillez remplir les informations suivantes :")

print("")

a = int(input("Entrez la valeur de a (NOMBRE ENTIER UNIQUEMENT) : "))
if a == 0:
    print("La valeur de A que vous venez d'entrer est incorrecte, ARRÊT DU PROGRAMME")
    print("Code erreur 0x000001a")
    print("Une erreur a été rencontrée, nous ne pouvons pas calculer, veuillez réessayer")
else:
    print("")

    b = float(input("Entrez la valeur de b (NOMBRE DÉCIMAL UNIQUEMENT) : "))
    if b == 0:
        print("La valeur de B que vous venez d'entrer est incorrecte, ARRÊT DU PROGRAMME")
        print("Code erreur 0x000001b")
        print("Une erreur a été rencontrée, nous ne pouvons pas calculer, veuillez réessayer")
    else:
        print("")

        print("Vous aurez en bas de cette page le résultat de ax=b")
        print("")
        print("Voici les différents résultats :")
        print("")
        print("La valeur de a additionnée à la valeur de b est égale à :")
        print(a + b)
        print("La valeur de a multipliée par la valeur de b est égale à :")
        print(a * b)
        print("La valeur de a divisée par la valeur de B est égale à :")
        print(a / b)
        print("La valeur de a soustraite par la valeur de b est égale à :")
        print(a - b)
        print("")
        print("La valeur de a élevée à la puissance de B est égale à :")
        print(a ** b)
        print("La valeur de la racine carrée de B est égale à :")
        print(a // b)
        print("La valeur du reste de la division de a par b est égale à :")
        print(a % b)
        print("")
        print("Résultat de ax=b :")
        print(b / a)
        print("")

        print("Le programme a réussi à résoudre votre problème !")
        print("")
        print("Pour rappel, la version de ce programme est la 4.5")

        print("")
        choix = input("Souhaitez-vous calculer le périmètre ou l'aire du disque ? (p/a) : ")
        if choix.lower() == "p":
            rayon = float(input("Entrez la valeur du rayon du disque (NOMBRE DÉCIMAL UNIQUEMENT) : "))
            perimetre = 2 * math.pi * rayon
            print("Le périmètre du disque de rayon", rayon, "est :", perimetre)
        elif choix.lower() == "a":
            rayon = float(input("Entrez la valeur du rayon du disque (NOMBRE DÉCIMAL UNIQUEMENT) : "))
            aire_disque = math.pi * rayon ** 2
            print("L'aire du disque de rayon", rayon, "est :", aire_disque)
        else:
            print("Choix invalide. Le programme se termine. NB : Veuillez entrer 'p' pour calculer le périmètre ou 'a' pour calculer l'aire du disque.")
recommencer = input("Voulez-vous relancer le programme ? (oui/non) ")

if recommencer.lower() == "oui":
    # Relancer le programme
    print("\n\n")  # Ajoutez des lignes vides pour plus de lisibilité
    exec(open(__file__).read())
else:
    print("Merci d'avoir utilisé le calculateur. Au revoir !")
