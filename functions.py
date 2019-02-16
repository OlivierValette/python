print("\nFonctions")


def monconcat(ch1, ch2="(nom inconnu)"):
    return ch1+" "+ch2


chaine = monconcat("John", "Doe")
print(chaine)
chaine = monconcat("John")
print(chaine)


def courses(nb_pommes, nb_poires, taux=0.055):
    prix_pommes = 5
    prix_poires = 2
    return (nb_pommes*prix_pommes+nb_poires*prix_poires)*(1+taux)


print("\nFonction calculant le prix des courses")
print("prix des courses : ", courses(4, 2))
# alternative : print("prix des courses : {0}".format(courses(4,2))


def switchcar(chaine, substit, frequence=2):
    liste = list(chaine)
    for i in range(0, len(liste)):
        if i % frequence == 0:
            liste[i] = substit
    return "".join(liste)


print("\nFonction substituant un caractère")
print("Ceci est un test -> ", switchcar("Ceci est un test", "_", 3) )


def initiales(etudiants):
    inits = []
    for etudiant in etudiants:
        inits.append(etudiant[0])
    return inits


print("\nInitiales des étudiants")
students = ["Nano", "Sterren", "Julia", "Melvin", "Mam"]
print(initiales(students))


def nomscyc(liste, letter):
    noms = []
    for item in liste:
        if item[0] == item[len(item)-1].upper() and item[0] == letter.upper():
            noms.append(item)
    return noms


print("\nNoms ciblés avec lettre")
students = ["Nano", "Sterren", "Julia", "Melvin", "Mam"]
print(nomscyc(students, "m"))


def caps(ecole, classe, maj=True):
    for i, eleve in enumerate(ecole[classe]):
        if maj:
            # passage en majuscules
            ecole[classe][i] = eleve.upper()
        else:
            # passage en minuscules, excepté la première lettre
            liste = list(eleve.lower())
            liste[0] = liste[0].upper()
            ecole[classe][i] = "".join(liste)
    return None


print("\nNoms en majuscule pour la classe DC2")
dc = {"DCDEV": students, "DC2": ["Bruno", "Valérie", "Agathe", "Benoît"]}
caps(dc, "DC2")
print(dc["DC2"])
caps(dc, "DC2", False)
print(dc["DC2"])


def minmax(ecole):
    kmax = ""
    kmin = list(ecole.keys())[0]
    for k in list(ecole.keys()):
        if len(k) > len(kmax):
            kmax = k
        if len(k) < len(kmin):
            kmin = k
    return kmin, kmax


def classemm(ecole, max=True):
    kmin, kmax = minmax(ecole)
    if max:
        return kmax, ecole[kmax]
    else:
        return kmin, ecole[kmin]


print("\nListe des étudiants pour la classe au nom le plus long")
print("Classe {0} - Liste d'élèves : {1}".format(classemm(dc)[0], classemm(dc)[1]))
print("\nListe des étudiants pour la classe au nom le plus court")
print("Classe {0} - Liste d'élèves : {1}".format(classemm(dc, False)[0], classemm(dc, False)[1]))

# (Rechercher sur google pour l’explication du fonctionnement de cet algorithme).
