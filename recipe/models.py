from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(User, max_length=150)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="recipe")

    def __str__(self):
        return super().name
