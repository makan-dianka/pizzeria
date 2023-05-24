from django.db import models
from .typefood import TypeFood

class Food(models.Model):
    type = models.ForeignKey(TypeFood, on_delete=models.CASCADE, related_name="type_food")
    nom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="pizza")
    desc = models.TextField(blank=True)
    prix = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.nom}"