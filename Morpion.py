plateau = [" " for _ in range(9)]

# On affiche le plateau avant chaque coup de chaque joueur
def afficherPlateau(p, gagnant=None):
     print(" " + p[0] + " | " + p[1] + " | " + p[2] + " ")
     print("---+---+---")
     print(" " + p[3] + " | " + p[4] + " | " + p[5] + " ")
     print("---+---+---")
     print(" " + p[6] + " | " + p[7] + " | " + p[8] + " ")
     if gagnant:
         print("""* Terminé ! Le joueur {0} a gagné la partie. *""".format(gagnant))


def morpion():
        joueur = "X"
        tour = 0

        # Tant que la partie est en cours...
        while True:
         # On affiche le plateau
         afficherPlateau(plateau)
         print("Tour du joueur " + joueur + ". Entrez un nombre de 1 à 9.")
         # -1 car range(9) va de 0 à 8
         move = int(input()) - 1

         # Si la case que le joueur a choisit est vide, on remplace l'esapce vide par le X ou le O.
         if plateau[move] == " ":
            plateau[move] = joueur
            tour += 1
         else:
            print("Cette case est déjà occupée, choisissez-en une autre.")
            continue
         
         # Toutes les combinaisons gagnantes
         if plateau[0] == plateau[1] == plateau[2] != " " \
         or plateau[3] == plateau[4] == plateau[5] != " " \
         or plateau[6] == plateau[7] == plateau[8] != " " \
         or plateau[0] == plateau[3] == plateau[6] != " " \
         or plateau[1] == plateau[4] == plateau[7] != " " \
         or plateau[2] == plateau[5] == plateau[8] != " " \
         or plateau[0] == plateau[4] == plateau[8] != " " \
         or plateau[2] == plateau[4] == plateau[6] != " ":
             afficherPlateau(plateau, joueur)
             break
               
         if tour == 9:
             afficherPlateau(plateau)
             print("Personne n'a gagné !")
             break
               
         joueur = "O" if joueur == "X" else "X"
           

if __name__ == "__main__":
    morpion()
