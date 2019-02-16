dico = {"texte": "texte1"}
if("texte" in dico):
    print("texte est dedans")
elif("texte2" in dico):
    print("texte2 est dedans")
else:
    print("rien dedans")

for i in range(0,3):
    print(i)

print("---")
liste = [1, 1.1, "texte"]
while ("texte" in liste):
    del liste[1:]
    print(liste)

print("---")
liste = [1, 1.1, "texte"]
for i, k in enumerate(liste):
    print(i, ": ", k)

print("---")
dico = {1: 1.1, "texte": None, "Poids": 200}
for k in list(dico.keys()):
    print(k, ": ", dico[k])

print("---")
for (k, v) in zip(list(dico.keys()), list(dico.values())):
    print(k, ": ", v, "(=", dico[k], "->", v==dico[k], ")")

print("---")
liste = [1, 1.1, "texte"]
for item in liste:
    if item == 1.1:
        print("trouvé")
        break   # ou bien : continue
    print(item)

print("---")
pommes = {"prix": 5, "qt": 3}
poires = {"prix": 2, "qt": 2}
taux = 0.055
totalHT = pommes["qt"]*pommes["prix"]+poires["qt"]*poires["prix"]
tva = round(taux * totalHT, 2)
totalTTC = totalHT + tva
if totalTTC >= 20:
    print("Coût supérieur à 20 €")
elif totalTTC >= 15:
    print("Coût supérieur à 15 €")
else:
    print("Courses inférieures à 15€")

print("---")
chaine = "Exemple de texte"
print(chaine)
liste = list(chaine)
for i in range(0, len(liste)):
    if i % 2 != 0:
        liste[i] = " "
chaine = "".join(liste)
print(chaine)

print("---")
print("\nNoms des étudiants de la classe DCDEV, avec initiales")
students = ["Nano", "Sterren", "Julia", "Melvin", "Mam"]
for student in students:
    if student[0] == student[len(student)-1].upper():
        print(student, student[0], "- ce nom se termine comme il commence")
    else:
        print(student, student[0])

print("---")
dc = {"DCDEV": students, "DC2": ["Bruno", "Valerie"]}
print(dc)
print("\nNoms en majuscule pour la classe DCDEV")
for i in range(0, len(dc["DCDEV"])):
    dc["DCDEV"][i] = dc["DCDEV"][i].upper()
print(dc)

print("\nListe des étudiants pour la classe au nom le plus long")
kmax = ""
for k in list(dc.keys()):
    if len(k) > len(kmax):
        kmax = k
print("classe : ", kmax, " - Liste d'élèves : ", dc[kmax])
