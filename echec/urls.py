from django.conf.urls import url,include

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
    url(r'^deplacement_roi$',views.Deplacement_roiView.as_view(),name='deplacement_roi'),
    url(r'^petit_roque$',views.Petit_roqueView.as_view(),name="petit_roque"),
    url(r'^grand_roque$',views.Grand_roqueView.as_view(),name="grand_roque"),
    url(r'^fourchette_pion$',views.Fourchette_pionView.as_view(),name="fourchettepion"),
    url(r'^fourchette_cavalier$',views.Fourchette_cavalierView.as_view(),name="fourchette_cavalier"),
    #url(r'^inscription$',views.inscription, name='inscription'),
    url(r'^rayon_x$',views.Rayon_xView.as_view(),name="rayon_x"),
    url(r'^clouage$',views.ClouageView.as_view(),name="clouage"),
	url(r'^Echiquier$',views.EchiquierView.as_view(),name='Echiquier'),
	url(r'^Maten1$',views.Maten1View.as_view(),name='Maten1'),
    url(r'^Maten2$',views.Maten2View.as_view(),name='Maten2'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^activate/account/$', views.activate_account, name='activate'),
    
]
