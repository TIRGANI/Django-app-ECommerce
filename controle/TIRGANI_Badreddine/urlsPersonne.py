from django.template.defaulttags import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('personnes/', views.personnes),

    path('addPersonne/', views.addPersonne),
    path('personne/createPer', views.createPer),
    path('personne/editPer/<int:id>', views.editPer),
    path('personne/deletePersonne/<int:id>', views.deletePersonne),
    path('personne/detailsPersonne/<int:id>', views.detailsPersonne),
    path('personne/editPersonne/<int:id>', views.editPersonne),
    path('personne/commandesPersonne/<int:id>', views.commandesPersonne),
    path('personne/searchPersonne', views.searchPersonne, name='search-personne'),
    path('personne/formulaire', views.FormPersonne),

]