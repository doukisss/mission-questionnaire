import json
import os
import unittest
from unittest.mock import patch
import questionnaire
import questionnaire_import

def additionner(a, b):
    return a + b 

def soustraire(a, b):
    return a - b 

def conversion_nombre():
    num_str = input("veuillez saisir un chiffre")
    return int(num_str) 

class TestUnitareDemo(unittest.TestCase):
    def setUp(self):  # -> None:
        # return super().setUp()
        print("setUp")
        
    def tearDown(self): # -> None:
        # return super().tearDown()
        print("tearDown")
    
    def test_additionner(self):
        print("additionner")
        self.assertEqual(additionner(10, 5), 15)
        self.assertEqual(additionner(10, 11), 21)
        self.assertEqual(additionner(10, 25), 35)

        
    def test_soustraire(self):
        print("soustraire")
        self.assertEqual(soustraire(10, 5), 5)
        self.assertEqual(soustraire(10, 11), -1)
        self.assertEqual(soustraire(10, 25), -15)
        
    def test_conversion_nbre_valide(self):
        with patch("builtins.input", return_value="100"):
            self.assertEqual(conversion_nombre(), 100)
            
    def test_conversion_entree_invalide(self):
        with patch("builtins.input", return_value="abcd"):
            self.assertRaises(ValueError, conversion_nombre)
            
            
class TestQuestion(unittest.TestCase):
    def test_question_bonne_mauvaise_reponse(self):
        choix = ("choix1", "choix2", "choix3")
        q = questionnaire.Question("titre question", choix, "choix2")
        with patch("builtins.input", return_value="1"):
            self.assertFalse(q.poser(1, 1))
        with patch("builtins.input", return_value="2"):
            self.assertTrue(q.poser(1, 1))
        with patch("builtins.input", return_value="3"):
            self.assertFalse(q.poser(1, 1))
            
            
class TestQuestionnaire(unittest.TestCase):
    def test_questionnaire_lancer_alien_debutant(self):
        filename = os.path.join("test_data", "cinéma_alien_débutant.json")
        q = questionnaire.Questionnaire.from_json_file(filename) 
        nb_question = len(q.questions)
        self.assertIsNotNone(q)
        self.assertEqual(q.categorie, "Cinéma")
        self.assertEqual(q.difficulte, "débutant")
        self.assertEqual(q.titre, "Alien")
        self.assertEqual(nb_question, 10)
        
        with patch("builtins.input", return_value="1"):
            q.lancer()
            self.assertEqual(q.lancer(), 1)

    def test_questionnaire_format_invalide(self):
        filename = os.path.join("test_data", "json_invalide1.json")
        q = questionnaire.Questionnaire.from_json_file(filename) 
        self.assertIsNotNone(q)
        self.assertEqual(q.categorie, "Inconnu")
        self.assertEqual(q.difficulte, "Inconnu")
        self.assertIsNotNone(q.questions)

        filename = os.path.join("test_data", "json_invalide2.json")
        q = questionnaire.Questionnaire.from_json_file(filename) 
        self.assertIsNone(q)
        
        filename = os.path.join("test_data", "json_invalide3.json")
        q = questionnaire.Questionnaire.from_json_file(filename) 
        self.assertIsNone(q)
        
        
class TestImportQuestionnaire(unittest.TestCase):
    def test_import_format_json(self):
        questionnaire_import.generate_json_file("Animaux", "Les chats", "https://www.codeavecjonathan.com/res/mission/openquizzdb_50.json")
        filenames = ("animaux_leschats_débutant.json", "animaux_leschats_confirmé.json", "animaux_leschats_expert.json")
        for filename in filenames:
            self.assertTrue(os.path.isfile(filename))
            file = open(filename, "r")
            json_data = file.read()
            file.close
            try:
                data = json.loads(json_data)
            except:
                print("Problème de désérialisation du fichier: " + filename)
              
            self.assertIsNotNone(data.get("titre"))
            self.assertIsNotNone(data.get("categorie"))
            self.assertIsNotNone(data.get("questions"))
            self.assertIsNotNone(data.get("difficulte"))
            for question in data.get("questions"):
                self.assertIsNotNone(question.get("titre"))
                self.assertIsNotNone(question.get("choix"))
                for choix in question.get("choix"):
                    self.assertGreater(len(choix[0]), 0)
                    self.assertTrue(isinstance(choix[1], bool))
                bonne_reponse = [i[0] for i in question.get("choix") if i[1]]
                self.assertEqual(len(bonne_reponse), 1)
     
    
unittest.main()