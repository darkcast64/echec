from django.shortcuts import render

from django.views.generic import TemplateView

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
