#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_socketio import SocketIO, send, emit
from flask import render_template
import threading
import os
import RPi.GPIO as GPIO
import time

# Association des broches aux devices
BR_BUZ = 22
BR_LUM = 27
BR_MVT = 17


# Temperature sensor
class TemperatureSensor:

    def __init__(self, code):
        self.address = code
        # Chemin du fichier contenant la température (remplacer par votre valeur trouvée précédemment)
        self.device_file = '/sys/bus/w1/devices/' + code + '/w1_slave'
        self.temperatureC = 0
        self.temperatureF = 0

    # Méthode qui lit dans le fichier température
    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    #  Méthode qui lit la temperature en Celsius
    def read_temp(self):
        lines = self.read_temp_raw()
        # Tant que la première ligne ne vaut pas 'YES', on attend 0,2s
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        # On cherche le '=' dans la seconde ligne du fichier
        equals_pos = lines[1].find('t=')
        # Si le '=' est trouvé, on converti ce qu'il y a après le '=' en degrés Celsius
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            self.temperatureC = round(temp_c, 0)
            self.temperatureF = round(temp_c * 9 / 5 + 32, 0)
            return 0


# Light sensor
class LightSensor:

    def __init__(self):
        self.light = 0

    # Méthode lecture lumière
    def read_light(self):
        # initialisation de la variable de lumière
        lightcount = 0
        GPIO.setup(BR_LUM, GPIO.OUT)
        GPIO.output(BR_LUM, GPIO.LOW)
        time.sleep(0.1)    # on draine la charge du condensateur
        GPIO.setup(BR_LUM, GPIO.IN)
        # Tant que la broche lit ‘off’ on incrémente notre variable
        while GPIO.input(BR_LUM) == GPIO.LOW:
            lightcount += 1
        self.light = lightcount
        return lightcount


# Initialisation des devices
def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Initialisation du buzzer
    GPIO.setup(BR_BUZ, GPIO.OUT)
    # Initialisation du détecteur de mouvements en GPIO 17 pour recevoir un signal
    GPIO.setup(BR_MVT, GPIO.IN)
    # Initialisation des broches pour le sensor de température
    os.system('modprobe w1-gpio')  # Allume le module 1wire
    os.system('modprobe w1-therm')  # Allume le module Temperature
    # sensor de température
    sensort = TemperatureSensor('28-01131a3eb0d1')
    sensort.read_temp()
    print("Sonde de température initialisée, T° =", sensort.temperatureC)
    # Initialisation du sensor de lumière
    sensorl = LightSensor()
    sensorl.read_light()
    print("Détecteur de lumière initialisé, L =", sensorl.light)
    return {"T": sensort, "L": sensorl}


# Boucle de lecture des détecteurs
def event_loop(sensors):
    previousstate = 0
    while True:
        # Acquisition de la température
        sensors["T"].read_temp()
        # Envoi de la temperature sur socket
        socketio.emit('temperature', sensors["T"].temperatureC, Broadcast=True)
        # Acquisition de la lumière
        sensors["L"].read_light()
        # Envoi de la temperature sur socket
        socketio.emit('lumen', sensors["L"].light, Broadcast=True)
        # Lecture du détecteur de mouvements
        currentstate = GPIO.input(BR_MVT)
        # Si le capteur est déclenché
        if currentstate == 1 and previousstate == 0:
            print("    Mouvement détecté !")
            # Levée de doute temperature
            message = "    Alerte annulée !"
            if sensors["T"].temperatureC < 28:
                mytime = time.localtime()
                # Levée de doute éclairage (le jour uniquement)
                if (mytime.tm_hour < 6 or mytime.tm_hour > 18) or sensors["L"].light < 100:
                    # GPIO.output(BR_BUZ, GPIO.HIGH)     # <--- Désactivation du buzzer
                    socketio.emit('alert', False, Broadcast=True)
                    message = "    Alerte confirmée !"
            print(message)
            # En enregistrer l'état
            previousstate = 1
        # Si le capteur s'est stabilisé
        elif currentstate == 0 and previousstate == 1:
            print("    Prêt")
            # GPIO.output(BR_BUZ, GPIO.LOW)      # <--- Désactivation du buzzer
            socketio.emit('alert', True, Broadcast=True)
            previousstate = 0
        # On attends 500ms
        time.sleep(0.5)


app = Flask(__name__)
socketio = SocketIO(app)

sondes = init_gpio()


# Socket de lecture des messages en provenance du client
@socketio.on('auth')
def handle_message(message):
    print("Code reçu de l'utilisateur: " + message['data'])


# Thread qui va permettre à notre fonction de se lancer en parallèle du serveur.
read_events = threading.Thread(target=event_loop, args=(sondes, ))
read_events.start()


@app.route("/")
def index():
    return render_template('index.html')
