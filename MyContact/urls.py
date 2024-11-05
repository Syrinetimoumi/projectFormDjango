from django.urls import path
from . import views

urlpatterns = [
    # Autres URL existantes
    
    # URL pour gérer le formulaire de contact
    path('form1/', views.controleform1, name='controleform1'),
    path('controleform2/', views.controleform2, name='controleform2'),
    path('controleform3/', views.controleform3, name='controleform3'),
]
