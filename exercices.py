# Exercice 1 :
# Un commerçant accorde une remise de 5 % pour tout achat d’un montant compris entre 100
# et 500 € et 8 % au-delà. Écrire un programme de calcul du montant de la remise sur un
# achat donné.


def remise(montant):
    MT1 = 100
    MT2 = 500
    REM1 = 0.05
    REM2 = 0.08
    if montant > MT2:
        return round(montant*(1 - REM2),2)
    elif montant > MT1:
        return round(montant*(1 - REM1),2)
    else:
        return montant


print('\nExercice 1')
print('\nCalcul de remise')
amount = float(input('Montant de la commande ? '))
print('Montant :', amount, ' Montant remisé : ', remise(amount))


# Exercice 2 :
# Ecrire un programme affichant une suite de nombres pairs dans une plage déterminée par
# l’utilisateur. Ce dernier entre au clavier une borne basse, ainsi qu’une borne haute, et le
# programme affiche dans un ordre croissant les nombres pairs compris dans ce domaine,
# sans inclure les bornes.


def pairs(b1, b2):
    liste = []
    for i in range(b1 + 1, b2):
        if i % 2 == 0:
            liste.append(i)
    return  liste


print('\nExercice 2')
print('\nAffichage des nombres pairs')
borne1 = int(input('Entre : '))
borne2 = int(input('et : '))
print(pairs(borne1, borne2))


# Exercice 3 :
# Ecrire un programme effectuant la multiplication de deux entiers naturels en utilisant
# uniquement l’opération d’addition.


def multiadd(int1, int2):
    result = 0
    for i in range(0, min(int1, int2)):
        result = result + max(int1, int2)
    return result


print('\nExercice 3')
print("\nProduit de 12 par 24 : ", multiadd(12, 24))
print("Produit de 51 par 8 : ", multiadd(51, 8))


# Ecrire un programme qui détermine si une chaîne de caractère donnée est un palindrome.
# Rappelons qu’un palindrome est un mot qui se lit « dans les deux sens », comme par
# exemple « laval ».


def palindrome(chaine):
    taille = len(chaine)
    if taille%2 == 0:
        return False
    imax = (taille - 1) // 2
    for i in range(0, imax):
        if chaine[i] != chaine[taille - 1 - i]:
            return False
    return True


print('\nExercice 4')
print('\nPalindrome')
texte = input('Mot à tester ? ')
if palindrome(texte):
    print('Le mot "', texte, '" est un palindrome !')
else:
    print('Le mot "', texte, '" n\'est pas un palindrome !')


# Exercice 5 :
# Ecrire un algorithme qui demande un nombre de départ, et qui ensuite affiche les
# dix nombres suivants. Par exemple, si l'utilisateur entre le nombre 17, le
# programme affichera les nombres de 18 à 27.


def suivants(n):
    liste = []
    for i in range(n+1, n+11):
        liste.append(i)
    return liste


print('\nExercice 5')
print('\nAffichage des 10 nombres suivants')
borne = int(input('Start : '))
print(suivants(borne))

# Exercice 6 :
# Ecrire une fonction indiquant si un élément est présent ou non dans une liste. S’il
# est présent cette fonction retournera l’indice de la case où il se trouve pour la
# première fois, et s’il est absent elle retournera -1.


def cherche(cible, meule):
    index = 0
    for item in meule:
        if item == cible:
            return index
        index += 1
    index = -1
    return index


print('\nExercice 6')
mot = "abcdefghijklmnopqrstuv"
liste = list(mot)
val = input('Texte à chercher : ')
if cherche(val, liste) == -1:
    print(val, "est absent de", liste)
else:
    print(val, "est présent dans", liste, "à l'indice", cherche(val, liste))

# Exercice 7 :
# Ecrire une fonction calculant le plus petit élément d’une liste de données numériques.
print('\nExercice 7')


# Exercice 8 :
# Ecrire une procédure réalisant le tri à bulles d’une liste de données numériques
print('\nExercice 8')
