import tkinter as tk
from tkinter import messagebox
from gestion_fichiers import gestionFichiers


class interfaceGraphique():
    """
    Classe pour l'interface graphique de l'application permettant de gérer les questionnaires.
    """
    def __init__(self):
        """Initialisation de l'interface graphique"""
        self.fenetre = tk.Tk()
        self.fenetre.title("Gestionnaire de questionnaires")
        self.fenetre.geometry("600x400")

        self.bg_color = "#4A90E2"
        self.button_color = "#0F4C81"
        self.button_active_color = "#0A3B6E"
        self.entry_bg = "#FFFFFF"
        self.label_fg = "#FFFFFF"

        self.fenetre.configure(bg=self.bg_color)
        self.action_frame = tk.Frame(self.fenetre, bg=self.bg_color)
        self.action_frame.pack(pady=10)
        self.content_frame = tk.Frame(self.fenetre, bg=self.bg_color)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.action = None
        self.afficher_actions()
    

    def afficher_actions(self):
        """Affiche les actions disponibles"""
        actions = [
            ("Créer un nouveau questionnaire", self.creer_questionnaire),
            ("Ajouter une question à un questionnaire existant", self.ajouter_question),
            ("Afficher les questions d'un questionnaire", self.afficher_questions),
            ("Supprimer un questionnaire", self.supprimer_questionnaire),
            ("Quitter", self.fenetre.destroy),
        ]
        for label, callback in actions:
            if callback is None:
                self.creer_bouton(label, state=tk.DISABLED, parent=self.action_frame)
            else:
                self.creer_bouton(label, callback, parent=self.action_frame)

    def creer_bouton(self, texte, commande=None, state=tk.NORMAL, parent=None):
        if parent is None:
            parent = self.content_frame
        bouton = tk.Button(
            parent,
            text=texte,
            command=commande,
            state=state,
            bg=self.button_color,
            fg=self.label_fg,
            activebackground=self.button_active_color,
            activeforeground=self.label_fg,
            relief=tk.RAISED,
            bd=2,
            padx=10,
            pady=5,
        )
        bouton.pack(pady=10)
        return bouton

    def clear_formulaire(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def creer_label(self, texte):
        label = tk.Label(
            self.content_frame,
            text=texte,
            bg=self.bg_color,
            fg=self.label_fg,
        )
        label.pack(pady=5)
        return label
        
    def creer_questionnaire(self):
        """Affiche les éléments pour créer un nouveau questionnaire"""
        self.clear_formulaire()
        self.creer_label("Nom du questionnaire:")
        self.entry_nom = tk.Entry(self.content_frame, bg=self.entry_bg, fg="black")
        self.entry_nom.pack(pady=10)
        self.creer_bouton("Créer", self.creer_fichier)
    
    def creer_fichier(self):
        """Crée un nouveau fichier questionnaire avec le nom spécifié"""
        nom_fichier = self.entry_nom.get()
        # Appeler la méthode de gestionFichiers pour créer le fichier
        gestionFichiers().creer_fichier(nom_fichier)
        messagebox.showinfo("Succès", f"Le questionnaire '{nom_fichier}' a été créé avec succès.")
        self.clear_formulaire()
    
    def ajouter_question(self):
        """Affiche les éléments pour ajouter une question à un questionnaire existant"""
        liste_questionnaires = gestionFichiers().lister_fichiers()
        if not liste_questionnaires:
            messagebox.showwarning("Aucun questionnaire", "Aucun questionnaire existant trouvé. Veuillez en créer un d'abord.")
        else:
            self.afficher_formulaire_ajout_question(liste_questionnaires)

    def afficher_formulaire_ajout_question(self, questionnaires: list):
        """Affiche le formulaire pour choisir un questionnaire et saisir une nouvelle question."""
        self.clear_formulaire()
        self.var_selection = tk.StringVar(self.fenetre)
        self.var_selection.set(questionnaires[0])
        menu = tk.OptionMenu(self.content_frame, self.var_selection, *questionnaires)
        menu.config(bg=self.button_color, fg=self.label_fg, activebackground=self.button_active_color, activeforeground=self.label_fg, highlightthickness=0)
        menu["menu"].config(bg=self.bg_color, fg="black")
        menu.pack(pady=10)

        self.creer_label("Intitulé de la question:")
        self.entry_question = tk.Entry(self.content_frame, width=60, bg=self.entry_bg, fg="black")
        self.entry_question.pack(pady=5)

        self.creer_label("Réponses (séparées par des virgules):")
        self.entry_reponses = tk.Entry(self.content_frame, width=60, bg=self.entry_bg, fg="black")
        self.entry_reponses.pack(pady=5)

        self.creer_bouton("Ajouter la question", self.valider_ajout_question)

    def valider_ajout_question(self):
        """Valide les données du formulaire et ajoute la question au questionnaire sélectionné."""
        nom_questionnaire = self.var_selection.get()
        intitule = self.entry_question.get().strip()
        reponses_raw = self.entry_reponses.get().strip()

        if not intitule:
            messagebox.showerror("Champ manquant", "L'intitulé de la question ne peut pas être vide.")
            return
        if not reponses_raw:
            messagebox.showerror("Champ manquant", "Veuillez saisir au moins une réponse.")
            return

        reponses = [r.strip() for r in reponses_raw.split(',') if r.strip()]
        if not reponses:
            messagebox.showerror("Format invalide", "Veuillez saisir des réponses valides séparées par des virgules.")
            return

        question = {
            "intitule": intitule,
            "reponses": reponses,
        }

        gestionFichiers().ajouter_question(nom_questionnaire, question)
        messagebox.showinfo("Succès", f"La question a été ajoutée au questionnaire '{nom_questionnaire}'.")

        self.clear_formulaire()

    def menu_deroulant(self, options: list=[]):
        """
        Affiche un menu déroulant
        Paramètres:
            options: La liste des options à afficher dans le menu déroulant
        """
        self.clear_formulaire()
        self.var_selection = tk.StringVar(self.fenetre)
        self.var_selection.set(options[0])
        menu = tk.OptionMenu(self.content_frame, self.var_selection, *options)
        menu.config(bg=self.button_color, fg=self.label_fg, activebackground=self.button_active_color, activeforeground=self.label_fg, highlightthickness=0)
        menu["menu"].config(bg=self.bg_color, fg="black")
        menu.pack(pady=10)

    def afficher_questions(self):
        """Affiche les éléments pour afficher les questions d'un questionnaire existant"""
        liste_questionnaires = gestionFichiers().lister_fichiers()
        if not liste_questionnaires:
            messagebox.showwarning("Aucun questionnaire", "Aucun questionnaire existant trouvé. Veuillez en créer un d'abord.")
        else:
            self.afficher_formulaire_affichage_questions(liste_questionnaires)

    def afficher_formulaire_affichage_questions(self, questionnaires: list):
        """Affiche le formulaire pour choisir un questionnaire et afficher ses questions."""
        self.clear_formulaire()
        self.var_selection = tk.StringVar(self.fenetre)
        self.var_selection.set(questionnaires[0])
        menu = tk.OptionMenu(self.content_frame, self.var_selection, *questionnaires)
        menu.config(bg=self.button_color, fg=self.label_fg, activebackground=self.button_active_color, activeforeground=self.label_fg, highlightthickness=0)
        menu["menu"].config(bg=self.bg_color, fg="black")
        menu.pack(pady=10)

        self.creer_bouton("Afficher les questions", self.valider_affichage_questions)
    
    def valider_affichage_questions(self):
        """Affiche les questions du questionnaire sélectionné."""
        nom_questionnaire = self.var_selection.get()
        questions = gestionFichiers().lister_questions(nom_questionnaire)
        if not questions:
            messagebox.showinfo("Aucune question", f"Aucune question trouvée dans le questionnaire '{nom_questionnaire}'.")
        else:
            messagebox.showinfo("Questions", f"Questions du questionnaire '{nom_questionnaire}':\n\n" + "\n".join(questions))
        self.clear_formulaire()
    
    def supprimer_questionnaire(self):
        """Affiche les éléments pour supprimer un questionnaire existant"""
        liste_questionnaires = gestionFichiers().lister_fichiers()
        if not liste_questionnaires:
            messagebox.showwarning("Aucun questionnaire", "Aucun questionnaire existant trouvé. Veuillez en créer un d'abord.")
        else:
            self.afficher_formulaire_suppression_questionnaire(liste_questionnaires)

if __name__ == "__main__":
    app = interfaceGraphique()
    app.fenetre.mainloop()
