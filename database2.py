# -*- coding: utf-8 -*-

import peewee

# Database creation
db = peewee.SqliteDatabase("courses2.db3")


class Courses2(peewee.Model):

    apple = peewee.IntegerField()
    pear = peewee.IntegerField()
    amount = peewee.FloatField()

    class Meta:
        database = db


# si fichier "main" (fichier d'amorçage)
if __name__ == "__Main__":
    try:
        Courses2.create_table()
    except peewee.OperationalError:
        print("Table already exists")


class Courses:

    PRIX_POM = 5
    PRIX_POI = 6

    def __init__(self, nb_pommes, nb_poires, tva=0.055):
        self.apple = nb_pommes
        self.pear = nb_poires
        self.vat = tva
        self.amount = self.montant()

    def montant(self):
        try:
            self.amount = round((self.apple * self.PRIX_POM + self.pear * self.PRIX_POI) * (1 + self.vat), 2)
        except TypeError as e:
            print("Conversion automatique de la saisie en entiers")
            self.apple = int(self.apple)
            self.pear = int(self.pear)
            self.amount = self.montant()
        finally:
            return self.amount

    def sauvegarder_db_orm(self):
        try:
            newrow = Courses2.create(apple=self.apple, pear=self.pear, amount=self.amount)\
            newrow.save()
        except peewee.OperationalError:
            print("Database error")

    def afficher_courses_db_orm(self):
        try:
            courses = Courses2.get()
            print("\nListe des courses")
            for course in courses:
                print('- ' + str(course.apple) + ' pommes + ' + str(course.pear) + ' poires - ' + str(course.amount) + "€")
        except peewee.OperationalError:
            print("Database error")


mescourses = Courses(5, 7)
mescourses.sauvegarder_db_orm()

lescourses = Courses(22, 31)
lescourses.sauvegarder_db_orm()

lescourses.afficher_courses_db_orm()
