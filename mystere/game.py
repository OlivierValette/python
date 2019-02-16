# -*- coding: utf-8 -*-
from random import randrange
import os
import sys
import sqlite3


class Game:
    P_WIDE = 100
    _counter = 0

    def __init__(self):
        Game._counter += 1
        self.id = Game._counter
        self.mystery = randrange(Game.P_WIDE)
        self.try_count = 0
        self.cx = self.db_start()
        if self.cx is None:
            sys.exit(1)

    # Database creation (drop before if necessary)
    def db_start(self):
        cnx = None
        try:
            # create a Connection object
            cnx = sqlite3.connect('score.db3')
            # create a Cursor object
            cur = cnx.cursor()
            sql_create_table = """
                CREATE TABLE IF NOT EXISTS scores (
                    rowid integer PRIMARY KEY,
                    game_id INT, 
                    player_name TEXT, 
                    win SMALLINT, 
                    hits INT
                ); """
            cur.execute(sql_create_table)
            cnx.commit()
        except sqlite3.Error as e:
            print("Database error {}:".format(e.args[0]))
        return cnx

    def try_again(self):
        ask_again = True
        while ask_again:
            ask = input('Donnez un nombre entre 0 et 100 :')
            try:
                try_value = int(ask)
                ask_again = False
            except ValueError :
                print('Erreur de saisie...')

        self.try_count += 1
        if try_value == self.mystery:
            print('Vous avez gagné en', self.try_count, "essais")
            return 0
        elif try_value > self.mystery:
            print('Trop grand')
            return 1
        else:
            print('Trop petit')
            return -1

    def game_save(self, player, rc):
        # SQLite database version
        csr = self.cx.cursor()
        csr.execute("INSERT INTO scores (game_id, player_name, win, hits) VALUES (?, ?, ?, ?)",
                    (self.id, player.fname, not rc, self.try_count)
                    )
        self.cx.commit()
        # flat file version
        if not os.path.isfile("scores.txt"):
            f = open("scores.txt", "w")
            f.write("Résultats du jeu mystère\n")
            f.close()
        f = open("scores.txt", "a+")
        result = "a perdu"
        if rc == 0:
            result = "a gagné en " + str(self.try_count) + " essais"
        f.write("Jeu " + str(self.id) + " - " + player.fname + " " + result + "\n")
        f.close()

    def game_topten(self):
        # SQLite database version
        csr = self.cx.cursor()
        csr.execute("""
            SELECT player_name, win, hits, game_id
            FROM scores
            WHERE win = 1
            order by hits ASC
            """)
        rows = csr.fetchall()
        print("\nMystery game Top-ten :")
        for row in rows:
            print(' Joueur : ' + str(row[0]) + ' - en ' + str(row[2]) + ' coups (jeu ' + str(row[3]) + ")")
        # flat file version
        # print('\n')
        # f = open("scores.txt", "r")
        # print(f.read())
        # f.close()
