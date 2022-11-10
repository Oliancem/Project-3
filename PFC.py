from random import *

def choix_utilisateur():
    joueur = input("Choisir entre : Pierre / Papier / Ciseaux / Puit:\n")
    while joueur not in ["Pierre","Papier","Ciseaux","Puit"]:
        joueur = input("Pierre\nPapier\nCiseaux\nPuit\n")
    return(joueur)
def choix_ordinateur():
    n = randint(1,3)
    if n == 1:
        IA = "Pierre"
    if n == 2:
        IA = "Papier"
    if n == 3:
        IA = "Ciseaux"
    return(IA)

a = choix_utilisateur()
b = choix_ordinateur()
print("\nVous avez choisit :", a)
print("Ordinateur à choisit :", b)

if a == "Pierre" and b == "Ciseaux":
    print("Gagné")
elif a == "Pierre" and b == "Papier":
    print("Perdu")
elif a == "Pierre" and b == "Pierre":
    print("Egalité")

if a == "Papier" and b == "Pierre":
    print("Gagné")
elif a == "Papier" and b == "Ciseaux":
    print("Perdu")
elif a == "Papier" and b == "Papier":
    print("Egalité")

if a == "Ciseaux" and b == "Papier":
    print("Gagné")
elif a == "Ciseaux" and b == "Pierre":
    print("Perdu")
elif a == "Ciseaux" and b == "Ciseaux":
    print("Egalite")

if a == "Puit" and b == "Papier":
    print("Gagné")
elif a == "Puit" and b == "Pierre":
    print("Gagné")
elif a == "Puit" and b == "Ciseaux":
    print ("Gagné")
