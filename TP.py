# Exercice 1 :
# Dans une école primaire, une classe a un niveau, un instituteur, et contient des élèves.
# Chaque élève a un nom, un prénom, une date de naissance, et aura dix notes dans l’année.
import datetime


# 1. Créer les deux classes nécessaires pour gérer l’école
class Eleve:

    counter = 0

    def __init__(self, nom, prenom, date):
        Eleve.counter += 1
        self.id = Eleve.counter
        self.firstname = nom
        self.lastname = prenom
        self.birthdate = date
        self.marks = []
        print("Elève", self.firstname, self.lastname, "créé avec l'identifiant", self.id)


class Classe:

    def __init__(self, niveau, instit, eleves=[]):
        self.level = niveau
        self.teacher = instit
        self.students = eleves
        print('Classe', self.level, 'de', self.teacher, 'créée.')

    def affecte(self, eleves):
        if type(eleves) == str:
            self.students.append(eleves)
        if type(eleves) == list:
            self.students += eleves

    def liste(self):
        print("Liste des élèves de la classe", self.level, "de", self.teacher)
        for eleve in self.students:
            print(eleve.lastname.upper(), eleve.firstname,  "- né(e) le", eleve.birthdate.strftime("%x"))


# 2. Créer une classe avec une liste d’élèves vide
print("\nEXERCICE 1")
cm2 = Classe("CM2", "Jean Perrin")

# 3. Créer deux élèves et assignez les à une classe
jeanne = Eleve("Lemoine", "Jeanne", datetime.datetime(2010, 5, 17))
julien = Eleve("Hubert", "Julien", datetime.datetime(2009, 10, 22))
cm2.affecte([jeanne, julien])

# 4. Faire une méthode qui affiche les noms, prénoms de tous les élèves d’une classe
cm2.liste()

# 5. Faire en sorte que je puisse à tout moment savoir le nombre d’élèves que j’ai créé
# creating one more student for test purpose, leading to a total count of 3 students
thimote = Eleve("Valjean", "Thimoté", datetime.datetime(2011, 2, 9))

print("Nombre total d'élèves créés :", Eleve.counter)


# Exercice 2:
# Déclarer une classe temps possédant 4 attributs
# 1. Le nombre d’heures de la durée.
# 2. Le nombre de minutes de la durée.
# 3. Le nombre de secondes de la durée.
# 4. le nombre de tierces  de la durée
# On munira cette classe de méthodes :
# 1. Un constructeur. On vérifiera que les nombres d’heures, minutes, secondes sont bien
# supérieur à zéro, dans le cas contraire on les remplacera par leurs opposés. On fera
# également les conversions nécessaires pour que les nombres de minutes et de secondes
# soient strictement inférieurs à 60.
# 2. Une méthode réalisant l’affichage de la durée (sous la forme 3h10m00s00t).
# 3. Une méthode convertissant la durée en un nombre de secondes.
# 4. Une méthode ajoutant à la durée un nombre de secondes.


class Temps:

    def __init__(self, h, m, s, t):
        duree = [t, s, m, h]
        for i in range(0, 4):
            if duree[i] < 0:
                duree[i] = -duree[i]
        for i in range(0, 3):
                if duree[i] >= 60:
                    duree[i+1] += duree[i] // 60
                    duree[i] = duree[i] % 60
        self.hour = duree[3]
        self.minute = duree[2]
        self.second = duree[1]
        self.third = duree[0]

    def affiche(self):
        print("{0}h{1}mn{2}s{3}t".format(self.hour, self.minute, self.second, self.third))

    def convertir(self):
        seconds = round(self.third / 60 + self.second + self.minute * 60 + self.hour * 3600, 2)
        print("Durée en secondes :", seconds)
        return seconds

    def add(self, s):
        if s < 0:
            s = -s
        s = self.convertir() + s
        self.third = round((s - int(s)) * 60)
        s = int(s)
        self.second = s % 60
        s = s // 60
        self.minute = s % 60
        self.hour = s // 60
        self.affiche()


# Créer un objet durée, en utilisant des paramètres demandés à l’utilisateur
print("\nEXERCICE 2")
print("\nEntrez une durée en h, mn, s, t")
vh = int(input("Nombre d'heures ?"))
vm = int(input("Nombre de minutes ?"))
vs = int(input("Nombre de secondes ?"))
vt = int(input("Nombre de tierces ?"))
print("Durée entrée :", vh, vm, vs, vt)
duree1 = Temps(vh, vm, vs, vt)

# affichez la durée
duree1.affiche()

# convertissez la durée en seconde et afficher le résultat
duree1.convertir()

# demandez à l’utilisateur un nombre de secondes et ajoutez le à la durée
print("\nAjouter des secondes")
# ss = int(input("Nombre de secondes à ajouter ?"))
duree1.add(ss)

# Bonus Exercice 3:
# Soit un tableau dont les éléments valent soit 100, soit 89, soit 7.
# Ecrire une fonction python réarrangeant ces éléments de telle sorte que tous les 100
# se retrouvent au début, suivi de tous les 7, puis enfin de tous les 89.
# Exemple, la liste suivante : 89 89 100 89 89 7 100 7 89 89 7
# deviendra : 100 100 7 7 7 89 89 89 89 89 89.
# Ecrire une fonction qui parcourt la liste ainsi triée et affiche à la fin le nombre d’occurrences de chaque élément.


# regroupe les éléments "cible" après le premier élément "inf"
def reorder(liste, cible, inf):
    for i in range(1, len(liste)):
        if liste[i] == cible:
            j = i-1
            while j >= 0 and liste[j] != cible and liste[j] != inf:
                liste[j+1] = liste[j]
                liste[j] = cible
                j = j - 1
    return liste


def compteur(liste):
    decompte = {}
    for item in liste:
        if item in list(decompte.keys()):
            decompte[item] += 1
        else:
            decompte[item] = 1
    return decompte


print("\nEXERCICE 3")
liste1 = [89, 89, 100, 89, 89, 7, 100, 7, 89, 89, 7]
print(liste1)
liste2 = reorder(reorder(liste1, 100, 100), 7, 100)
print(liste2)

print(compteur(liste2))


from collections import Counter
print("Contrôle :", Counter(liste2))
