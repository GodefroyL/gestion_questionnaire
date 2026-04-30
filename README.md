## Application pour ajouter ou supprimer les questions

L'objectif de cette application est de faciliter l'ajout des questions pour l'application de questionnaire de films.

### Prérequis
- Dans le fichier config.json : ajouter le chemin vers les fichiers du questionnaire (dossier_du_questionnnaire/static/json/)

### Architecture du projet

- interface : classe pour la partie visible du site (IHM)
- main : fonction principale qui gère l'écriture des fichier
- gestion_fichiers : classe pour la gestion des fichiers (lecture, écriture...)
- config.json : fichier de configuration avec les liens pour les fichiers de questionnaire (fichier local non poussé sur git)

### Fonctionnement

- Menu déroulant pour choisir le fichier à modifier ou ajouter un fichier.
- Fenêtres avec champs à remplir avec question, réponse, catégorie (ou film pour les questionnaires par catégorie). Boutons pour revenir au menu déroulant principal.
- Ajout de la question dans le fichier.
- Retour à la fenêtre des champs à remplir.
