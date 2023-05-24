from django.db import models

class TypeFood(models.Model):
    food = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"{self.food}"