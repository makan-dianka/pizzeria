from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib import messages
import logging

from django.contrib.auth import(
                            authenticate,
                            login,
                            logout 
                            )

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pizzeria:orders')
        else:
            messages.info(request, 'Credential Incorrect')
    return render(request, "accounts/login.html")


def deconnexion(request):
    logout(request)
    return redirect('pizzeria:index')