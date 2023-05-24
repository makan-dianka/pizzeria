from django.urls import path
from . views import (
    food, index,  paiement, panier,
    orders,
    )

app_name = "pizzeria"

urlpatterns = [
    path('', index.index, name="index"),
    path('formules', food.food, name="food"),
    path('panier', panier.panier, name="panier"),
    path('paiement', paiement.paiement, name="paiement"),
    path('orders', orders.orders, name="orders"),
]