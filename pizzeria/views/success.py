from django.shortcuts import render


def success(request):
    return render(request, 'pizzeria/paiement_successful.html')