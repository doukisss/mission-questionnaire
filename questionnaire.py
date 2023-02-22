

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
import os, fnmatch
import glob
# from questionnaire import bonne_reponse


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def from_data_json(data):
        # ....
        choix = [i[0] for i in data["choix"]]
        bonne_reponse = [i[0] for i in data["choix"] if i[1]]
        if len(bonne_reponse) != 1:
            return None
        # print(choix)
        q = Question(data["titre"], choix, bonne_reponse[0])
        return q

    def poser(self):
        print("QUESTION: ")
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
    def __init__(self, questions, titre, categorie, difficulte):
        self.questions = questions
        self.titre = titre
        self.categorie = categorie
        self.difficulte = difficulte
        
    def from_data_json(data):
        questionnaire_data_questions = questionnaire_data["questions"]
        questions = [Question.from_data_json(i) for i in questionnaire_data_questions]
        return Questionnaire(questions, data["titre"], data["categorie"], data["difficulte"])
        

    def lancer(self):
        print("-----------------")
        print("QUESTIONNAIRE:", self.titre)
        print("Catégore:", self.categorie)
        print("Difficulté:", self.difficulte)
        print("Nombre de question:", str(len(self.questions)))
        print("-----------------")
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


# files=glob.glob("dossier_json/*")
# for i in range(0, len(files)):
# files = "animaux_leschats_expert.json"
files = os.listdir('.')
fichier = files[2]
file = open(fichier, "r")
json_data = file.read()
file.close()

questionnaire_data = json.loads(json_data)

# q = Question.FromJsonData(questionnaire_data_questions[0])
# q.poser()
Questionnaire.from_data_json(questionnaire_data).lancer()
print()