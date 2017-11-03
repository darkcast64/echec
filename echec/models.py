from django.db import models
from django.views.generic import TemplateView

# Create your models here.
class IndexView(TemplateView):
    template_name="templates/index.html"
