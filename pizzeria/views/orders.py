from django.shortcuts import render
from .. models.commande import Commande
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:connexion')
def orders(request):
    context = {}
    if request.method=="POST":
        try:
            search = Commande.objects.get(number=request.POST.get("cmdnumber").strip())
            context['get_element'] = search
        except:
            pass

        return render(request, "pizzeria/search.html", context)
    return render(request, "pizzeria/orders.html", context)