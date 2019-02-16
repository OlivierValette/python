#!/usr/bin/python
# -*- coding: UTF-8 -*-
from game import Game
from player import Player
from flask import Flask, render_template

app = Flask(__name__)


if __name__ == "mystery":

    # New game
    mystery = Game()
    print("Le jeu", mystery.id, "est prêt à démarrer")

    @app.route('/')
    def start_game():
        return render_template('index.html', id=mystery.id)

    @app.route('/game')
    def run_game():

        # Boucle de jeu
        again = True
        while again:

            # New player
            new_player = Player(input('Entrez votre prénom : '))

            # Same player shoot again
            while new_player.lives > 0:
                print('Il vous reste', new_player.lives, 'vies')
                rc = mystery.try_again()
                if rc == 0:
                    break
                else:
                    new_player.lose_live()

                if new_player.lives == 0:
                    print('Vous avez perdu')

            mystery.game_save(new_player, rc)
            print('Fin de jeu')

            if input('Voulez-vous rejouer (O/N) ?') in ["N", "n"]:
                again = False
        return render_template('game.html')

    @app.route('/topten')
    def end_game():
        mystery.game_topten()
        return render_template('topten.html')
