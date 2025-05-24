from django.urls import path
from . views import (
    connexion
    )

app_name = "accounts"

urlpatterns = [
    path('login/', connexion.connexion, name="connexion"),
    path('deconnexion/', connexion.deconnexion, name="deconnexion"),
]