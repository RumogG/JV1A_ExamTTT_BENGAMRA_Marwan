import random



#-----------------------------------------------------------------------------------------

def Check1 (a, b, c):

    if (a == ["X"]*3) or (a == ["O"]*3):
        return True
    elif (b == ["X"]*3) or (b == ["O"]*3):
        return True
    elif (c == ["X"]*3) or (c == ["O"]*3):
        return True
    else:
        return False

#-----------------------------------------------------------------------------------------


"""
Ligne = [0, 0, 0]
Ligne2 = [0, 0, 0]
Ligne3 = [0, 0, 0]


print(Ligne)
print(Ligne2)
print(Ligne3)
"""

victoire = False
equipe = "X"
tour = 1
team = 10
Ligne = [0, 0, 0]
Ligne2 = [0, 0, 0]
Ligne3 = [0, 0, 0]

while victoire == False:

    print("Tour", tour)
    print("Equipe", equipe)



    
    choix_ligne = int(input("Quelle ligne, 1, 2 ou 3 ?\n"))
    if choix_ligne > 3:
        print("Trop Grand!")
        choix_ligne = int(input("Quelle ligne, 1, 2 ou 3 ?\n"))

    choix_case = int(input("Quelle case, 1, 2 ou 3 ?\n"))-1
    if choix_case > 2:
        print("Trop Grand!")
        choix_case = int(input("Quelle case, 1, 2 ou 3 ?\n"))-1


    if choix_ligne == 1:
        Ligne[choix_case] = equipe
    elif choix_ligne == 2:
        Ligne2[choix_case] = equipe
    else:
        Ligne3[choix_case] = equipe


    print(Ligne)
    print(Ligne2)
    print(Ligne3)

    victoire = Check1(Ligne, Ligne2, Ligne3)
    if victoire == True:
        print("Victoire")

    team *= 2
    if team > 10 :
        equipe = "O"
        team = 5
    else:
        equipe = "X"
    
    tour +=1