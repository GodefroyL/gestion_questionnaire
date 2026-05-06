import os
import json
from interface import interfaceGraphique


def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    os.chdir(config["dossier_questionnaire_git"])

    os.system("git pull")
    app = interfaceGraphique()
    app.fenetre.mainloop()
    os.system("git add .")
    os.system('git commit -m "Mise à jour du projet"')
    os.system("git push")

if __name__ == "__main__":
    main()