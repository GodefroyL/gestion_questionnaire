import json
import os

class gestionFichiers:
    """
    Classe gestionFichiers pour gérer les interactions avec les fichiers contenant les questions
    """
    def __init__(self):
        with open("config.json") as f:
            self.fichier_config = json.load(f)
        self.dossier_questionnaire = self.fichier_config.get("dossier_questionnaire")
    
    def lister_fichiers(self):
        """Renvoie la liste des fichiers json présents dans le dossier sans l'extension"""
        fichiers = [f for f in os.listdir(self.dossier_questionnaire) if f.endswith(".json")]
        return [os.path.splitext(f)[0] for f in fichiers]

    def chemin_fichier(self, nom_fichier):
        """Reconstruire le chemin d'un fichier à partir de son nom"""
        return os.path.join(self.dossier_questionnaire, f'{nom_fichier}.json')
    
    def creer_fichier(self, nom_fichier: str, contenu: dict={}):
        """
        Crée un fichier json avec le contenu spécifié
        Paramètres:
            nom_fichier (str): Le nom du fichier à créer sans l'extension .json
            contenu (dict): Le contenu à écrire dans le fichier
        """
        chemin = f'{self.chemin_fichier(nom_fichier)}'
        with open(chemin, 'w') as f:
            json.dump(contenu, f, indent=4)
    
    def ajouter_question(self, nom_fichier: str, question: dict):
        """
        Ajoute une question à un fichier json existant
        Paramètres:
            nom_fichier (str): Le nom du fichier auquel ajouter la question sans l'extension .json
            question (dict): La question à ajouter au format {"question": "texte de la question", "reponses": ["réponse1", "réponse2", ...]}
        """
        chemin = self.chemin_fichier(nom_fichier)
        if not os.path.exists(chemin):
            print(f"Le fichier {nom_fichier}n'existe pas.")
            return
        
        with open(chemin, 'r') as f:
            contenu = json.load(f)
        
        question['id'] = len(contenu) + 1
        contenu.append(question)
        
        with open(chemin, 'w') as f:
            json.dump(contenu, f, indent=4)
    
    def lister_questions(self, nom_fichier: str):
        """
        Liste les questions d'un fichier json
        Paramètres:
            nom_fichier (str): Le nom du fichier à lire sans l'extension .json
        Retourne:
            list: Une liste de questions présentes dans le fichier
        """
        chemin = self.chemin_fichier(nom_fichier)
        if not os.path.exists(chemin):
            print(f"Le fichier {nom_fichier} n'existe pas.")
            return []
        
        with open(chemin, 'r') as f:
            contenu = json.load(f)
        
        return [q['intitule'] for q in contenu]


if __name__=='__main__':
    classe = gestionFichiers()
    print(classe.lister_fichiers())
