

# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#
import json
import os


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score




"""questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)"""

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)

"""Questionnaire(
    (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
    )
).lancer()"""


"""class QuestionnaireApi():
    def __init__(self, les_titres, les_choix, les_reponses):
        self.les_titres = les_titres
        self.les_choix = les_choix
        self.les_reponses = les_reponses"""

json_files = os.listdir('.')
fichier = json_files[3]
file = open(fichier, "r")
data = file.read()
file.close()
f = open("data_json.json", "w")
json.dump(data, f)
f.close()
"""json_string = json.dumps(data)
print(type(json_string))"""
data_dict = json.loads(data)
print(type(data_dict))
print(data_dict["questions"])
print(len(data_dict["questions"]))
titre = []
choix_booleen = []
bonne_reponse = []
for data in data_dict["questions"]:
    titre.append(data["titre"])
    choix_booleen.append(data["choix"])
    for i in data["choix"]:
        if i[1]:
            bonne_reponse.append(i[0])

questionnaire = []

for i in range(0, len(data_dict["questions"])):
    les_titres = titre[i]
    les_choix = choix_booleen[i]
    les_reponses = bonne_reponse[i]
choix = []
for i in choix_booleen:
    choix.append(i)


print((titre[0], choix_booleen[0], bonne_reponse[0]))
print((titre[0], choix[0], bonne_reponse[0]))
choix2 = []
for i in range(0, len(choix[0])):
    tor = choix[0][i][0]
    choix2.append(tor)
print(choix2)


# Questionnaire(Question(titre[0], choix2, bonne_reponse[0])).lancer()


"""Questionnaire(
    Question(titre[0], choix_booleen, bonne_reponse[0]),
).lancer()"""


Questionnaire(
    (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
    )
).lancer()


