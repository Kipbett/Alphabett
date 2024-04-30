from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('shoes/', views.shoes, name="shoes"),
    path('shoes/sneakers', views.sneakers, name="sneakers"),
    path('shoes/sliders', views.sliders, name="sliders"),
    path('shoes/football-boots', views.football_boots, name="football"),
    path('shoes/boots', views.boots, name="boots"),
    path('shoes/loafers', views.loafers, name="loafers"),
    path('shoes/flat-shoes', views.flat_shoes, name="flats"),
    path('watches/', views.watches, name="watches"),
    path('watches/men', views.watches_men, name="men"),
    path('watches/ladies', views.watches_ladies, name="ladies"),
    path('home-appliances/', views.home_appliances, name="home-appliances"),
    path('watches/kitchen-ware', views.kitchen_ware, name="kitchen-ware"),
    path('watches/utensils', views.utensils, name="utensils"),
    path('watches/kitchen_appliances', views.kitchen_appliances, name="kitchen-appliances"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)