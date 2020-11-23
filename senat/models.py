from django.db import models

class Senateur(models.Model):
    Matricule = models.TextField(null=True)
    Qualite = models.TextField(null=True)
    Nom_usuel = models.TextField(null=True)
    Prenom_usuel = models.TextField(null=True)
    Etat = models.TextField(null=True)
    Date_naissance = models.TextField(null=True)
    Date_de_deces = models.TextField(null=True)
    Groupe_politique = models.TextField(null=True)
    Type_d_app_au_grp_politique = models.TextField(null=True)
    Commission_permanente = models.TextField(null=True)
    Circonscription = models.TextField(null=True)
    Fonction_au_Bureau_du_Senat = models.TextField(null=True)
    Courrier_electronique = models.TextField(null=True)
    PCS_INSEE = models.TextField(null=True)
    Categorie_professionnelle = models.TextField(null=True)
    Description_de_la_profession = models.TextField(null=True)

    slug = models.TextField(unique=True)