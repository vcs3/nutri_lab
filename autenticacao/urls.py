from importlib.resources import path
from django.urls import path
from django.urls import include
from . import views

urlpatterns=[
    path('cadastro/', views.cadastro , name='cadastro'),
    path('logar/', views.logar , name='logar'),
    path('sair/', views.sair, name="sair"),
    path('ativar_conta/<str:token>/', views.ativar_conta, name="ativar_conta"),
    path('', include('plataforma.urls')),
    

]