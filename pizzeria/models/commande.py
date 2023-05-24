from django.contrib import admin
from django.db import models
from . order import OrderFood


class Commande(models.Model):
    username = models.CharField(max_length=100)
    useremail = models.EmailField(max_length=100)
    fk_orderfood = models.ManyToManyField(OrderFood)
    commentaire = models.TextField()
    carte = models.CharField(max_length=200)
    number = models.CharField(max_length=50, default="boul.ange!default")
    create_at = models.DateTimeField(auto_now_add=True)

class CommandeAdmin(admin.ModelAdmin):
    list_display = ['username', 'useremail', 'commentaire', 'carte', 'create_at']