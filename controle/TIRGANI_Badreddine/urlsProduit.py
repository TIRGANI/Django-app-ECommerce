from django.template.defaulttags import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('produits/', views.produits),

    path('addProduit/', views.addProduit),
    path('produit/createProd', views.createProd),
    path('produit/editProd/<int:id>', views.editProd),
    path('produit/deleteProduit/<int:id>', views.deleteProduit),
    path('produit/detailsProduit/<int:id>', views.detailsProduit),
    path('produit/editProduit/<int:id>', views.editProduit),
    path('produit/searchProduit', views.searchProduit, name='search-produit'),
    path('produit/formulaire', views.FormProduit),

]