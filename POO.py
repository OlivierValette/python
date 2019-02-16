import math


class Hotel:
    """
        Classe hôtel
    """
    # attributs de classe
    tauxtva = 0.20

    # constructeur
    def __init__(self, ville, nb_chambres, haspool):
        self.location = ville
        self.rooms = nb_chambres
        self.available = nb_chambres
        self.pool = haspool

    # méthodes
    def book(self):
        if self.available > 0:
            self.available -= 1
            return "Réservé"
        else:
            return "Complet"


hotelMonaco = Hotel("Monaco", 27, True)
# print('\nHôtel ', hotelMonaco.location, '\nNombre de chambres : ', hotelMonaco.rooms)
# if hotelMonaco.pool:
#     print('Avec piscine')

# print('Nombre de chambres libres : ', hotelMonaco.available)
# for i in range(0, hotelMonaco.rooms+1):
#     print('Demande de réservation : ', hotelMonaco.book())
#     print('Nombre de chambres libres : ', hotelMonaco.available)


class Courses:

    PRIX_POM = 5
    PRIX_POI = 6

    def __init__(self, nb_pommes, nb_poires, tva=0.055):
        self.apple = nb_pommes
        self.pear = nb_poires
        self.vat = tva

    def montant(self):
        return round((self.apple * self.PRIX_POM + self.pear * self.PRIX_POI) * (1 + self.vat), 2)


mescoures = Courses(5, 7)
print('Montant TTC des courses : ', mescoures.montant())


class Animal:

    def __init__(self, sex, age):
        self.sex = sex
        self.age = age

    def manger(self):
        print('Miam')

    def dormir(self):
        print('Zzzz')


class Humain(Animal):

    def __init__(self, sex, age, nom):
        Animal.__init__(self, sex, age)
        self.nom = nom

    def parler(self):
        print('Blabla')

    def manger(self):
        print(self.nom, 'dit "Miam"')


gorilla = Animal("M", 3)
hector = Humain("M", 27, "Hector")

gorilla.dormir()
hector.parler()
hector.manger()
gorilla.manger()

# Les véhicules
# écrire une classe Vehicule qui représente différents types de véhicules
# avec les attributs position_x, position_y, vitesse, marque, modele, niveau_carburant et conducteur
# avec les méthodes monter, descendre, avancer, stopper, faire_le_plein et reculer
# Le conducteur est un être humain
# Le véhicule n’a pas de conducteur au départ
# Le niveau de carburant du véhicule est vide au départ


class Vehicule:

    def __init__(self, position_x, position_y, marque, modele):
        self.position_x = position_x
        self.position_y = position_y
        self.vitesse = 0
        self.marque = marque
        self.modele = modele
        self.niveau_carburant = False
        self.conducteur = ""

    def monter(self, conducteur):
        if self.conducteur == "":
            self.conducteur = conducteur
        print("Conducteur ", self.conducteur.nom, 'en place')

    def descendre(self):
        if self.vitesse != 0:
            self.stopper()
        print(self.conducteur.nom, ' descend du véhicule')
        self.conducteur = ""
        print("Véhicule à l'arrêt, sans conducteur")

    def avancer(self, dx, dy):
        self.position_x += dx
        self.position_y += dy
        self.vitesse = round(math.sqrt(dx**2 + dy**2), 3)
        print('Véhicule avance à : (', self.position_x, ',', self.position_y, ") vitesse : ", self.vitesse)

    def reculer(self, dx, dy):
        if self.vitesse != 0:
            self.stopper()
        self.position_x -= dx
        self.position_y -= dy
        self.vitesse = round(math.sqrt(dx**2 + dy**2), 3)
        print('Véhicule recule à : (', self.position_x, ',', self.position_y, ") vitesse : ", self.vitesse)

    def stopper(self):
        self.vitesse = 0
        print('Véhicule arrêté')

    def faire_le_plein(self):
        if self.vitesse != 0:
            self.stopper()
        self.niveau_carburant = True
        print('Plein effectué')


# écrire une classe Voiture qui spécialise Vehicule
# avec la constante nombre_roues et avec l’attribut option_gps
class Voiture(Vehicule):

    NB_ROUES = 4

    def __init__(self, position_x, position_y, marque, modele, option_gps):
        Vehicule.__init__(self, position_x, position_y, marque, modele)
        self.option_gps = option_gps


# écrire une classe Avion qui spécialise Vehicule
# avec les méthodes décoller et atterrir
class Avion(Vehicule):

    def __init__(self, position_x, position_y, marque, modele):
        Vehicule.__init__(self, position_x, position_y, marque, modele)
        self.envol = False

    def decoller(self):
        self.envol = True
        print('Décollage effectué')

    def atterrir(self):
        self.envol = False
        print('Atterrissage effectué')


# écrire un programme qui simule trois êtres humains se déplaçant en avion et en voiture en respectant
# les contraintes des classes
hector = Humain("M", 27, "Hector")
juliette = Humain("F", 32, "Juliette")
pierre = Humain("H", 54, "Pierre")

print("\nHector prend une Fiat 500")
fiat500 = Voiture(0, 0, "Fiat", "500", False)
fiat500.monter(hector)
fiat500.faire_le_plein()
fiat500.avancer(50, 120)
fiat500.stopper()
fiat500.descendre()

print("\nJuliette pilote un avion à Roissy")
a320 = Avion(220, 550, "Airbus", "A320")
a320.monter(juliette)
a320.faire_le_plein()
a320.decoller()
a320.avancer(350, -830)
a320.atterrir()
a320.descendre()

