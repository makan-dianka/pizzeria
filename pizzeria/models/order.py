from django.db import models
from .food import Food

class OrderFood(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    def __str__(self) -> str:
        return f"{self.food} - {self.quantite}"