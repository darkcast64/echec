from django.shortcuts import render, redirect


from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from echec import helpers
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings




# Create your models here.
class IndexView(TemplateView):
    template_name="echec/index.html"
class ReglesView(TemplateView):
    template_name="echec/regles.html"
class CommandementsView(TemplateView):
    template_name="echec/10commandements.html"
class ProprietesView(TemplateView):
    template_name="echec/proprietes-strategiques.html"
class Deplacement_pionView(TemplateView):
    template_name="echec/deplacement_pion.html"
class Deplacement_cavalierView(TemplateView):
    template_name="echec/deplacement_cavalier.html"
class Deplacement_fouView(TemplateView):
    template_name="echec/deplacement_fou.html"
class Deplacement_tourView(TemplateView):
    template_name="echec/deplacement_tour.html"
class Deplacement_dameView(TemplateView):
    template_name="echec/deplacement_dame.html"
class Deplacement_roiView(TemplateView):
    template_name="echec/deplacement_roi.html"
class Petit_roqueView(TemplateView):
	template_name="echec/petitroque.html"
class Grand_roqueView(TemplateView):
	template_name="echec/grandroque.html"
class EchiquierView(TemplateView):
	template_name="echec/exercices.html"
class Fourchette_pionView(TemplateView):
	template_name="echec/fourchettepion.html"
class Fourchette_cavalierView(TemplateView):
	template_name="echec/fourchette_cavalier.html"
class Rayon_xView(TemplateView):
	template_name="echec/rayon_x.html"
class ClouageView(TemplateView):
	template_name="echec/clouage.html"
class Maten1View(TemplateView):
	template_name="echec/maten1.html"
class Maten2View(TemplateView):
    template_name="echec/maten2.html"


 #def inscription(request):
    #if request.method=="Post":
        #form = InscriptionForm(request.Post)
        #if form.is_valid():
            #form.save
            #return redirect('echec/accueil.html')
    #else:
        #form = InscriptionForm()

    #return render(request, 'echec/inscription.html',{'form' : form })


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserCreationForm()

    return render(request, 'echec/register.html', {'form': f})
    
