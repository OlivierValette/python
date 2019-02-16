import os.path


def division(a, b):
    try:
        print("a/b =", str(a/b))
    except TypeError as e:
        print('Les arguments doivent être des chiffres', e.__traceback__)
        return -1
    except ZeroDivisionError as e:
        print('Dénominateur nul', e.__cause__)
        return -1
    finally:
        return 0


division(1, 2)
division(1, "2")
division(1, 0)


class Courses:

    PRIX_POM = 5
    PRIX_POI = 6

    def __init__(self, nb_pommes, nb_poires, tva=0.055):
        self.apple = nb_pommes
        self.pear = nb_poires
        self.vat = tva

    def montant(self):
        try:
            amount = round((self.apple * self.PRIX_POM + self.pear * self.PRIX_POI) * (1 + self.vat), 2)
        except TypeError as e:
            print("Conversion automatique de la saisie en entiers")
            self.apple = int(self.apple)
            self.pear = int(self.pear)
            amount = self.montant()
        finally:
            return amount

    def liste_courses(self):
        if not os.path.isfile("courses.txt"):
            f = open("courses.txt", "w")
            f.write("Liste de courses :\n")
            f.close()
        f = open("courses.txt", "a+")
        f.write("- " + str(self.apple) + " Pommes\n")
        f.write("- " + str(self.pear) + " Poires\n")
        f.close()

    def afficher_courses(self):
        f = open("courses.txt", "r")
        print(f.read())
        f.close()


mescourses = Courses(5, "7")
print('Montant TTC des courses : ', mescourses.montant())
mescourses.liste_courses()

pom = input('Nombre de pommes ? : ')
poi = input('Nombre de poires ? : ')
lescourses = Courses(pom, poi)
print('Montant TTC des courses : ', lescourses.montant())
lescourses.liste_courses()

lescourses.afficher_courses()


