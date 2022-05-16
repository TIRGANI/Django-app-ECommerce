from django.db import models


class Personne(models.Model):
    #id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    email = models.CharField(max_length=45)


class Categorie(models.Model):
    #id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nomCategorie = models.CharField(max_length=45)


class Commande(models.Model):
    #id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    referenceCmd = models.CharField(max_length=45)
    dateCmd = models.DateField(max_length=45)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name='Personne', default=None)


class Produit(models.Model):
    produitRef = models.CharField(max_length=45)
    nomProduit = models.CharField(max_length=45)
    dateProduit = models.DateField(max_length=45)
    prix = models.FloatField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='Categorie', default=None)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='Commande', default=None)
