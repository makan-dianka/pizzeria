from django.shortcuts import render
from .. models.commande import Commande

def orders(request):
    orders = Commande.objects.all()
    context = {"orders" : orders}
    if request.method=="POST":
        try:
            search = Commande.objects.get(number=request.POST.get("cmdnumber").strip())
            context['get_element'] = search
        except:
            pass

        return render(request, "pizzeria/search.html", context)
    return render(request, "pizzeria/orders.html", context)