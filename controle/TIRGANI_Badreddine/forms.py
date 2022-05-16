from django import forms
from django.forms import ModelForm

from TIRGANI_Badreddine.models import Personne, Commande, Categorie, Produit

class GeneralForm(forms.Form):
    search = forms.CharField()

class PersonneForm(ModelForm):
    class Meta:
        model = Personne
        fields = ['id', 'nom', 'prenom', 'email']

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = ['id', 'referenceCmd', 'dateCmd', 'personne']

class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = ['id', 'nomCategorie']

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = ['id', 'produitRef', 'nomProduit', 'dateProduit', 'prix', 'categorie', 'commande']