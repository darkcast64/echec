from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import Truncator
from .forms import NouveauContactForm

# Create your views here.

def home(request):
	text="""<h1> Bienvenue sur mon blog</h1>"""
	return HttpResponse(text)

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def regles(request):
		return render(request,'blog/regles.html')

from .forms import ContactForm


def contact(request):

    # Construire le formulaire, soit avec les données postées,

    # soit vide si l'utilisateur accède pour la première fois

    # à la page.

    form = ContactForm(request.POST or None)

    # Nous vérifions que les données envoyées sont valides

    # Cette méthode renvoie False s'il n'y a pas de données 

    # dans le formulaire ou qu'il contient des erreurs.

    if form.is_valid(): 

        # Ici nous pouvons traiter les données du formulaire

        sujet = form.cleaned_data['sujet']

        message = form.cleaned_data['message']

        envoyeur = form.cleaned_data['envoyeur']

        renvoi = form.cleaned_data['renvoi']


        # Nous pourrions ici envoyer l'e-mail grâce aux données 

        # que nous venons de récupérer

        envoi = True

    

    # Quoiqu'il arrive, on affiche la page du formulaire.

    return render(request, 'blog/contact.html', locals())

def nouveau_contact(request):

    sauvegarde = False

    form = NouveauContactForm(request.POST or None, request.FILES)

    if form.is_valid():

        contact = Contact()

        contact.nom = form.cleaned_data["nom"]

        contact.adresse = form.cleaned_data["adresse"]

        contact.photo = form.cleaned_data["photo"]

        contact.save()

        sauvegarde = True


    return render(request, 'blog/nouveau_contact.html', {'form': form, 'sauvegarde': sauvegarde })


def voir_contacts(request):

   contacts = Contact.objects.all()

   return render(request, 'voir_contacts.html', {'contacts': contacts})

   })
