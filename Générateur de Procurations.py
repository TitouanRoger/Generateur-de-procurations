import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generer_procuration():
    mandant_nom = entry_nom_mandant.get()
    mandant_prenom = entry_prenom_mandant.get()
    mandant_date_naissance = entry_date_naissance_mandant.get()
    mandant_lieu_naissance = entry_lieu_naissance_mandant.get()
    mandant_adresse = entry_adresse_mandant.get()
    mandataire_nom = entry_nom_mandataire.get()
    mandataire_prenom = entry_prenom_mandataire.get()
    mandataire_date_naissance = entry_date_naissance_mandataire.get()
    mandataire_lieu_naissance = entry_lieu_naissance_mandataire.get()
    mandataire_adresse = entry_adresse_mandataire.get()
    sujet = entry_sujet.get()
    lieu_redaction = entry_lieu_redaction.get()

    if not all([mandant_nom, mandant_prenom, mandant_date_naissance, mandant_lieu_naissance,
                mandant_adresse, mandataire_nom, mandataire_prenom,
                mandataire_date_naissance, mandataire_lieu_naissance, lieu_redaction]):
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    date_redaction = datetime.today().strftime('%d/%m/%Y')

    texte_procuration = f"""
    Je soussigné(e) {mandant_nom} {mandant_prenom}, né(e) le {mandant_date_naissance} à {mandant_lieu_naissance},
    domicilié(e) au {mandant_adresse},
    donne procuration à {mandataire_nom} {mandataire_prenom}, né(e) le {mandataire_date_naissance} à {mandataire_lieu_naissance},
    domicilié(e) au {mandataire_adresse},
    pour {sujet}.

    Fait le {date_redaction} à {lieu_redaction}.

    Signature du mandant : ________________________

    Signature du mandataire : _____________________
    """
    messagebox.showinfo("Procuration Générée", texte_procuration)
    return texte_procuration

def ajouter_texte(canvas, texte, largeur_max):
    y_position = 750
    for ligne in texte.split("\n"):
        mots = ligne.split()
        ligne_courante = ""
        for mot in mots:
            if canvas.stringWidth(ligne_courante + " " + mot) < largeur_max:
                ligne_courante += " " + mot if ligne_courante else mot
            else:
                canvas.drawString(72, y_position, ligne_courante)
                y_position -= 14
                ligne_courante = mot
        canvas.drawString(72, y_position, ligne_courante)
        y_position -= 14

def telecharger_pdf():
    procuration_texte = generer_procuration()

    if not procuration_texte:
        return

    fichier_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

    if fichier_pdf:
        c = canvas.Canvas(fichier_pdf, pagesize=letter)
        width, height = letter

        ajouter_texte(c, procuration_texte, width - 144)

        c.save()
        messagebox.showinfo("Succès", "Le fichier PDF a été généré avec succès !")

root = tk.Tk()
root.title("Générateur de procurations")

tk.Label(root, text="Informations du mandant").pack()
entry_nom_mandant = tk.Entry(root, width=50)
entry_nom_mandant.pack()
entry_nom_mandant.insert(0, "Nom du mandant")

entry_prenom_mandant = tk.Entry(root, width=50)
entry_prenom_mandant.pack()
entry_prenom_mandant.insert(0, "Prénom du mandant")

entry_date_naissance_mandant = tk.Entry(root, width=50)
entry_date_naissance_mandant.pack()
entry_date_naissance_mandant.insert(0, "Date de naissance du mandant (JJ/MM/AAAA)")

entry_lieu_naissance_mandant = tk.Entry(root, width=50)
entry_lieu_naissance_mandant.pack()
entry_lieu_naissance_mandant.insert(0, "Lieu de naissance du mandant")

entry_adresse_mandant = tk.Entry(root, width=50)
entry_adresse_mandant.pack()
entry_adresse_mandant.insert(0, "Adresse complète du mandant")

tk.Label(root, text="Informations du mandataire").pack()
entry_nom_mandataire = tk.Entry(root, width=50)
entry_nom_mandataire.pack()
entry_nom_mandataire.insert(0, "Nom du mandataire")

entry_prenom_mandataire = tk.Entry(root, width=50)
entry_prenom_mandataire.pack()
entry_prenom_mandataire.insert(0, "Prénom du mandataire")

entry_date_naissance_mandataire = tk.Entry(root, width=50)
entry_date_naissance_mandataire.pack()
entry_date_naissance_mandataire.insert(0, "Date de naissance du mandataire (JJ/MM/AAAA)")

entry_lieu_naissance_mandataire = tk.Entry(root, width=50)
entry_lieu_naissance_mandataire.pack()
entry_lieu_naissance_mandataire.insert(0, "Lieu de naissance du mandataire")

entry_adresse_mandataire = tk.Entry(root, width=50)
entry_adresse_mandataire.pack()
entry_adresse_mandataire.insert(0, "Adresse complète du mandataire")

tk.Label(root, text="Sujet").pack()
entry_sujet = tk.Entry(root, width=50)
entry_sujet.pack()
entry_sujet.insert(0, "Sujet de la procuration")

tk.Label(root, text="Lieu de rédaction").pack()
entry_lieu_redaction = tk.Entry(root, width=50)
entry_lieu_redaction.pack()
entry_lieu_redaction.insert(0, "Lieu (ville) de rédaction")

tk.Button(root, text="Générer", command=generer_procuration).pack(pady=10)
tk.Button(root, text="Télécharger en PDF", command=telecharger_pdf).pack(pady=10)

root.mainloop()