from django.contrib import admin

# Register your models here.
from TIRGANI_Badreddine.models import Personne, Commande, Categorie, Produit


@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'prenom', 'email')
    ordering = ('id','nom', 'prenom', 'email')
    list_filter = ('id','nom', 'prenom', 'email')
    search_fields = ('id','nom', 'prenom', 'email')

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'referenceCmd', 'dateCmd', 'personne_id')
    ordering = ('id', 'referenceCmd', 'dateCmd', 'personne_id')
    list_filter = ('id', 'referenceCmd', 'dateCmd', 'personne_id')
    search_fields = ('id', 'referenceCmd', 'dateCmd', 'personne_id')

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomCategorie')
    ordering = ('id', 'nomCategorie')
    list_filter = ('id', 'nomCategorie')
    search_fields = ('id', 'nomCategorie')

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id', 'produitRef', 'nomProduit', 'dateProduit', 'prix', 'categorie_id', 'commande_id')
    ordering = ('id', 'produitRef', 'nomProduit', 'dateProduit', 'prix', 'categorie_id', 'commande_id')
    list_filter = ('id', 'produitRef', 'nomProduit', 'dateProduit', 'prix', 'categorie_id', 'commande_id')
    search_fields = ('id', 'produitRef', 'nomProduit', 'dateProduit', 'prix', 'categorie_id', 'commande_id')
