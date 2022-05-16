from django.template.defaulttags import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('commandes/', views.commandes),

    path('addCommande/', views.addCommande),
    path('commande/createCom', views.createCom),
    path('commande/editCom/<int:id>', views.editCom),
    path('commande/deleteCommande/<int:id>', views.deleteCommande),
    path('commande/detailsCommande/<int:id>', views.detailsCommande),
    path('commande/editCommande/<int:id>', views.editCommande),
    path('commande/searchCommande', views.searchCommande, name='search-commande'),
    path('commande/formulaire', views.FormCommande),

]