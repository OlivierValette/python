# Imports
import os
import time

# Initialisation des broches
os.system('modprobe w1-gpio')  # Allume le module 1wire
os.system('modprobe w1-therm')  # Allume le module Temperature


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
            self.temperatureC = round(temp_c, 2)
            self.temperatureF = round(self.convertCtoF(temp_c), 2)
            return 0

    #  Méthode qui converti la temperature en Fahrenheit
    def convertCtoF(self, tc):
        return tc * 9 / 5 + 32


# On affiche la température tant que le script tourne
while True:
    sonde = TemperatureSensor('28-0213121a4aaa')
    sonde.read_temp()
    print('Température de la sonde :', sonde.temperatureC, '°C -', sonde.temperatureF, '°F')
    time.sleep(1)
