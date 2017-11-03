from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^accueil$', views.IndexView.as_view(),name='accueil'),
    url(r'^regles$', views.ReglesView.as_view(),name='regles'),
    url(r'^commandements$', views.CommandementsView.as_view(),name='10commandements'),
    url(r'^proprietes-strategiques$', views.ProprietesView.as_view(),name='proprietes_strategiques'),
    url(r'^deplacement_pion$', views.Deplacement_pionView.as_view(),name='deplacement_pion'),
    url(r'^deplacement_cavalier$',views.Deplacement_cavalierView.as_view(),name='deplacement_cavalier'),
    url(r'^deplacement_fou$',views.Deplacement_fouView.as_view(),name='deplacement_fou'),
    url(r'^deplacement_tour$',views.Deplacement_tourView.as_view(),name='deplacement_tour'),
    url(r'^deplacement_dame$',views.Deplacement_dameView.as_view(),name='deplacement_dame'),
]
