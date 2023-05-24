from django.contrib import admin
from .models.typefood import TypeFood
from .models.food import Food
from . models.order import OrderFood
from . models.commande import Commande, CommandeAdmin

admin.site.register(Food)
admin.site.register(TypeFood)
admin.site.register(OrderFood)
admin.site.register(Commande, CommandeAdmin)
