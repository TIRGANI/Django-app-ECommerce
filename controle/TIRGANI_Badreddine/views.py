from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Personne, Produit, Categorie, Commande
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import GeneralForm, PersonneForm, CommandeForm, CategorieForm, ProduitForm


# index#################
def index(request):
    return render(request, 'includes/index.html')


# FORMULAIRES############
def GeneralSearch(request):
    form = GeneralForm()
    return render(request, "formTemplate.html", {"form": form})


def FormPersonne(request):
    form = PersonneForm()
    return render(request, "personne/formulairePersonne.html", {"form": form})


def FormCommande(request):
    form = CommandeForm()
    return render(request, "commande/formulaireCommande.html", {"form": form})


def FormCategorie(request):
    form = CategorieForm()
    return render(request, "categorie/formulaireCategorie.html", {"form": form})


def FormProduit(request):
    form = ProduitForm()
    return render(request, "produit/formulaireProduit.html", {"form": form})


# PERSONNES####################
# la liste des clients
def personnes(request):
    personnes_list = Personne.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(personnes_list, 10)
    try:
        personnes = paginator.page(page)
    except PageNotAnInteger:
        personnes = paginator.page(1)
    except EmptyPage:
        personnes = paginator.page(paginator.num_pages)
    context = {'personnes': personnes}
    return render(request, 'personne/personnes.html', context)


# pour afficher les détail d'un patient
def detailsPersonne(request, id):
    personnes = Personne.objects.get(id=id)
    context = {'personnes': personnes}
    return render(request, 'personne/detailsPersonne.html', context)


# pour supprimer un patient et redireger l'utilisateur vers index
def deletePersonne(request, id):
    try:
        personne = Personne.objects.get(id=id)
    except Personne.DoesNotExist:
        return redirect('/personnes')
    personne.delete()
    return redirect('/personnes')


# pour modifier un patient et redireger l'utilisateur vers index
def editPersonne(request, id):
    personne = Personne.objects.get(id=id)
    context = {'personne': personne}
    return render(request, 'personne/editPersonne.html', context)


def editPer(request, id):
    nom = request.POST.get("nom", "").capitalize()
    prenom = request.POST.get("prenom", "")
    email = request.POST.get("email", "")
    personne = Personne(id=id, nom=nom, prenom=prenom, email=email)
    personne.save()
    return redirect("/personnes")


# les deux views suivants pour modifier le Créer ajouter un patient
def addPersonne(request):
    return render(request, "personne/addPersonne.html")


def createPer(request):
    nom = request.POST.get("nom", "").capitalize()
    prenom = request.POST.get("prenom", "")
    email = request.POST.get("email", "")
    personne = Personne.objects.create(nom=nom, prenom=prenom, email=email)
    personne.save()
    return redirect("/personnes")


def searchPersonne(request):
    searched = request.POST['searched']
    clients_searched = Personne.objects.filter(nom__contains=searched)
    page = request.GET.get('page', 1)
    paginator = Paginator(clients_searched, 10)
    try:
        personnes = paginator.page(page)
    except PageNotAnInteger:
        personnes = paginator.page(1)
    except EmptyPage:
        personnes = paginator.page(paginator.num_pages)
    context = {'personnes': personnes}
    return render(request, 'personne/personnes.html', context)


# PRODUITS####################
# la liste des clients
def produits(request):
    produits_list = Produit.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(produits_list, 10)
    try:
        produits = paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)
    context = {'produits': produits}
    return render(request, 'produit/produits.html', context)


# pour afficher les détail d'un patient
def detailsProduit(request, id):
    produits = Produit.objects.get(id=id)
    context = {'produits': produits}
    return render(request, 'produit/detailsProduit.html', context)


# pour supprimer un patient et redireger l'utilisateur vers index
def deleteProduit(request, id):
    try:
        produit = Produit.objects.get(id=id)
    except Produit.DoesNotExist:
        return redirect('/produits')
    produit.delete()
    return redirect('/produits')


# pour modifier un patient et redireger l'utilisateur vers index
def editProduit(request, id):
    produit = Produit.objects.get(id=id)
    categories = Categorie.objects.all()
    commandes = Commande.objects.all()
    context = {'produit': produit,'categories':categories,'commandes':commandes}
    return render(request, 'produit/editProduit.html', context)


def editProd(request, id):
    produitRef = request.POST.get("produitRef", "")
    nomProduit = request.POST.get("nomProduit", "")
    dateProduit = request.POST.get("dateProduit")
    prix = request.POST.get("prix", "")
    produit = Produit(id=id, produitRef=produitRef, nomProduit=nomProduit, dateProduit=dateProduit, prix=prix)
    produit.save()
    return redirect("/produits")


# les deux views suivants pour modifier le Créer ajouter un patient
def addProduit(request):
    categories = Categorie.objects.all()
    commandes = Commande.objects.all()
    context = {'categories': categories, 'commandes': commandes}
    return render(request, "produit/addProduit.html", context)


def createProd(request):
    produitRef = request.POST.get("produitRef", "")
    nomProduit = request.POST.get("nomProduit", "")
    dateProduit = request.POST.get("dateProduit")
    prix = request.POST.get("prix", "")
    categorie_id = request.POST.get("categorie", "")
    categorie = Categorie.objects.get(id=categorie_id)
    commande_id = request.POST.get("commande", "")
    commande = Commande.objects.get(id=commande_id)
    produit = Produit(produitRef=produitRef, nomProduit=nomProduit, dateProduit=dateProduit, prix=prix,
                      categorie=categorie, commande=commande)
    produit.save()
    return redirect("/produits")


def searchProduit(request):
    searched = request.POST['searched']
    clients_searched = Produit.objects.filter(produitRef__contains=searched)
    page = request.GET.get('page', 1)
    paginator = Paginator(clients_searched, 10)
    try:
        produits = paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)
    context = {'produits': produits}
    return render(request, 'produit/produits.html', context)


# CATEGORIES####################
# la liste des clients
def categories(request):
    categories_list = Categorie.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(categories_list, 10)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    context = {'categories': categories}
    return render(request, 'categorie/categories.html', context)


# pour afficher les détail d'un patient
def detailsCategorie(request, id):
    categories = Categorie.objects.get(id=id)
    context = {'categories': categories}
    return render(request, 'categorie/detailsCategorie.html', context)


# pour supprimer un patient et redireger l'utilisateur vers index
def deleteCategorie(request, id):
    try:
        categorie = Categorie.objects.get(id=id)
    except Categorie.DoesNotExist:
        return redirect('/categories')
    categorie.delete()
    return redirect('/categories')


# pour modifier un patient et redireger l'utilisateur vers index
def editCategorie(request, id):
    categorie = Categorie.objects.get(id=id)
    context = {'categorie': categorie}
    return render(request, 'categorie/editCategorie.html', context)


def editCat(request, id):
    nomCategorie = request.POST.get("nomCategorie", "")
    categorie = Categorie(id=id, nomCategorie=nomCategorie)
    categorie.save()
    return redirect("/categories")


# les deux views suivants pour modifier le Créer ajouter un patient
def addCategorie(request):
    return render(request, "categorie/addCategorie.html")
    # return redirect("/categories")


def createCat(request):
    nomCategorie = request.POST.get("nomCategorie", "")
    categorie = Categorie(nomCategorie=nomCategorie)
    categorie.save()
    return redirect("/categories")


def searchCategorie(request):
    searched = request.POST['searched']
    clients_searched = Categorie.objects.filter(nomCategorie__contains=searched)
    page = request.GET.get('page', 1)
    paginator = Paginator(clients_searched, 10)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    context = {'categories': categories}
    return render(request, 'categorie/categories.html', context)


# COMMANDES####################
# la liste des clients
def commandes(request):
    commandes_list = Commande.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(commandes_list, 10)
    try:
        commandes = paginator.page(page)
    except PageNotAnInteger:
        commandes = paginator.page(1)
    except EmptyPage:
        commandes = paginator.page(paginator.num_pages)
    context = {'commandes': commandes}
    return render(request, 'commande/commandes.html', context)


# pour afficher les détail d'un patient
def detailsCommande(request, id):
    commandes = Commande.objects.get(id=id)
    context = {'commandes': commandes}
    return render(request, 'commande/detailsCommande.html', context)


# pour supprimer un patient et redireger l'utilisateur vers index
def deleteCommande(request, id):
    try:
        commande = Commande.objects.get(id=id)
    except Commande.DoesNotExist:
        return redirect('/commandes')
    commande.delete()
    return redirect('/commandes')


# pour modifier un patient et redireger l'utilisateur vers index
def editCommande(request, id):
    personne = Personne.objects.all()
    commande = Commande.objects.get(id=id)
    context = {'commande': commande, 'personnes': personne}
    return render(request, 'commande/editCommande.html', context)


def editCom(request, id):
    referenceCmd = request.POST.get("referenceCmd", "")
    dateCmd = request.POST.get("dateCmd")
    commande = Commande(id=id, referenceCmd=referenceCmd, dateCmd=dateCmd)
    commande.save()
    return redirect("/commandes")


# les deux views suivants pour modifier le Créer ajouter un patient
def addCommande(request):
    perssones = Personne.objects.all()
    context = {'personnes': perssones}
    return render(request, "commande/addCommande.html", context)
    # return redirect("/categories")


def createCom(request):
    referenceCmd = request.POST.get("referenceCmd", "")
    dateCmd = request.POST.get("dateCmd")
    personne_id = request.POST.get("personne", "")
    personne = Personne.objects.get(id=personne_id)
    commande = Commande(referenceCmd=referenceCmd, dateCmd=dateCmd, personne=personne)
    commande.save()
    return redirect("/commandes")


def searchCommande(request):
    searched = request.POST['searched']
    clients_searched = Categorie.objects.filter(referenceCmd__contains=searched)
    page = request.GET.get('page', 1)
    paginator = Paginator(clients_searched, 10)
    try:
        commandes = paginator.page(page)
    except PageNotAnInteger:
        commandes = paginator.page(1)
    except EmptyPage:
        commandes = paginator.page(paginator.num_pages)
    context = {'commandes': commandes}
    return render(request, 'commande/commandes.html', context)


def commandesPersonne(request, id):
    commandes_list = "none"
    commandes_list = Commande.objects.filter(personne_id=id)
    taille = len(commandes_list)
    if taille == 0:
        operations_list = "none"
        context = {'commandes': commandes_list}
        return render(request, 'commande/commandes.html')
    else:
        page = request.GET.get('page', 1)
        paginator = Paginator(commandes_list, 10)
        try:
            commandes = paginator.page(page)
        except PageNotAnInteger:
            commandes = paginator.page(1)
        except EmptyPage:
            commandes = paginator.page(paginator.num_pages)
        context = {'commandes': commandes}
        return render(request, 'commande/commandes.html', context)
