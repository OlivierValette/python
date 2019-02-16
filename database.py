# -*- coding: utf-8 -*-

import sqlite3
import sys

# Database creation (drop before if necessary)
cnx = None
try:
    # create a Connection object
    cnx = sqlite3.connect('courses.db3')
    # create a Cursor object
    cur = cnx.cursor()
    cur.execute("DROP TABLE IF EXISTS courses")
    cur.execute("CREATE TABLE courses (rowid INTEGER PRIMARY KEY, npommes INT, npoires INT, montant FLOAT)")
    cnx.commit()
except sqlite3.Error as e:
    print("Database error {}:".format(e.args[0]))
    sys.exit(1)


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

    def addto_courses_db(self):
        cx = None
        try:
            cx = sqlite3.connect('courses.db3')
            csr = cx.cursor()
            csr.execute("INSERT INTO courses (npommes, npoires, montant) VALUES (?, ?, ?)",
                        (self.apple, self.pear, self.montant()))
            cx.commit()
        except sqlite3.Error as e:
            if cx:
                cx.rollback()
            print("Database error {}:".format(e.args[0]))
            sys.exit(1)

    def afficher_courses(self):
        try:
            cx = sqlite3.connect('courses.db3')
            csr = cx.cursor()
            csr.execute("SELECT ROWID, npommes, npoires, montant FROM courses")
            rows = csr.fetchall()
            print("\nListe des courses")
            for row in rows:
                print('- ' + str(row[1]) + ' pommes + ' + str(row[2]) + ' poires - ' + str(row[3]) + "€ (" + str(row[0]) + ")")
        except sqlite3.Error as e:
            print("Database error {}:".format(e.args[0]))
            sys.exit(1)


mescourses = Courses(5, "7")
# print('Montant TTC des courses : ', mescourses.montant(), "€")
mescourses.addto_courses_db()

lescourses = Courses(22, 31)
# print('Montant TTC des courses : ', lescourses.montant(), "€")
lescourses.addto_courses_db()

lescourses.afficher_courses()
