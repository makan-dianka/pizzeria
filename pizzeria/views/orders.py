from django.shortcuts import render
from .. models.commande import Commande

def orders(request):
    orders = Commande.objects.all()

    context = {"orders" : orders}
    return render(request, "pizzeria/orders.html", context)