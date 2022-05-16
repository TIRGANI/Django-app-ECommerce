from django.template.defaulttags import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories),

    path('addCategorie/', views.addCategorie),
    path('categorie/createCat', views.createCat),
    path('categorie/editCat/<int:id>', views.editCat),
    path('categorie/deleteCategorie/<int:id>', views.deleteCategorie),
    path('categorie/detailsCategorie/<int:id>', views.detailsCategorie),
    path('categorie/editCategorie/<int:id>', views.editCategorie),
    path('categorie/searchCategorie', views.searchCategorie, name='search-categorie'),
    path('categorie/formulaire', views.FormCategorie),

]