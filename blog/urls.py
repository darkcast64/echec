from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
    url(r'^regles$',views.regles),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^nouveau_contact/$', views.nouveau_contact, name='nouveau_contact'),
    url(r'^voir_contacts/$',views.voir_contacts),
]
