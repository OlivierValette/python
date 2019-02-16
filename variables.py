pommes = {"prix": 5, "qt": 3}
poires = {"prix": 2, "qt": 2}
taux = 0.055
totalHT = pommes["qt"]*pommes["prix"]+poires["qt"]*poires["prix"]
tva = round(taux * totalHT, 2)
print(tva)
totalTTC = totalHT + tva
print(totalTTC)

texte = "Le python s'est encore échappé !"
stexte = texte[16:22]
print(stexte)

students = ["nano", "sterren", "julia", "melvin"]
print("Nombre d'étudiants : " + str(len(students)))
students.append("julien")
print(students)

dc = {"DCDEV": students}
print(dc)
dc["DCPRO"] = []
print(dc)
dc["DCPREPA"] = []
print(dc)
dc["DCPRO"].append("Bruno")
print(dc)
dc.pop('DCPREPA')
print(dc)
