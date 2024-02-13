from django.urls import path
from AppCoder import views

urlpatterns= [
    path('', views.inicio, name = "Inicio"),
    path('lista/', views.lista, name = "lista"),
    path('buscar/', views.buscar, name = "buscar"),
    path('tiendas/', views.tiendas, name = "tiendas"),
    path('descuentos/', views.descuentos, name = "descuentos"),
]