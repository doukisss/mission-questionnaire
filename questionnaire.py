

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
import sys
# from questionnaire import bonne_reponse


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def from_data_json(data):
        # Transform les données choix tuple (titre, boot "bonne reponse") -> [choix1, choix2, ...]
        choix = [i[0] for i in data["choix"]]
        # Trouve le bon choix en fonction du bool "bonne reponse"
        bonne_reponse = [i[0] for i in data["choix"] if i[1]]
        # Si aucune bonne reponse ou plusieurs bonnes réponses -> Anomalie dans les données
        if len(bonne_reponse) != 1:
            return None
        # print(choix)
        q = Question(data["titre"], choix, bonne_reponse[0])
        return q

    def poser(self, num_question, nb_question):
        print(f"QUESTION: {num_question} / {nb_question}" )
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
    
    def from_json_file(file_name):
        #file_name = os.listdir('.')
        #fichier = file_name[2]
        try:
            file = open(file_name, "r")
            json_data = file.read()
            file.close()
            questionnaire_data = json.loads(json_data)
        except:
            print("Exception lors de l'ouverture de la lecture du fichier")
            return None
        return Questionnaire.from_data_json(questionnaire_data)
        
        
    def from_data_json(data):
        if not data.get("categorie"):
            data["categorie"] = "Inconnu"
        if not data.get("difficulte"):
            data["difficulte"] = "Inconnu"
        if not data.get("titre"):
            return
        if not data.get("questions"):
            return
        
            
        questionnaire_data_questions = data["questions"]
        questions = [Question.from_data_json(i) for i in questionnaire_data_questions]
        # supprime les questions None (qui n'ont pas pu être créé)
        questions = [i for i in questions if i]
        return Questionnaire(questions, data["titre"], data["categorie"], data["difficulte"])
        

    def lancer(self):
        self.nb_question = len(self.questions)
        print("-----------------")
        print("QUESTIONNAIRE:", self.titre)
        print("Catégore:", self.categorie)
        print("Difficulté:", self.difficulte)
        print("Nombre de question:", str(self.nb_question))
        print("--------------------")
        
        score = 0
        for i in range(self.nb_question):
            question = self.questions[i]
            # print("QUESTION:", i + 1, "/", str(len(self.questions)))
            if question.poser(i+1, self.nb_question):
                score += 1
        print("Score final :", score, "sur", self.nb_question)
        return score


# files=glob.glob("dossier_json/*")
# for i in range(0, len(files)):
# files = "animaux_leschats_expert.json"

if __name__ == "__main__":

    print(sys.argv)

    if len(sys.argv) < 2:
        print("Vous devez entrer le nom d'un fichier au format json")
        exit(0)
    json_filename = sys.argv[1]
    questionnaire = Questionnaire.from_json_file(json_filename)
    if questionnaire:
        questionnaire.lancer()

        
