from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}"


class Ingredient(models.Model):
    name = models.CharField(max_length=55, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class DishType(models.Model):
    name = models.CharField(max_length=55, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=55, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.SET_DEFAULT,
        null=True,
        default="Tasty food",
        related_name="types",
    )
    cooks = models.ManyToManyField(Cook, related_name="dish")
    ingredient = models.ManyToManyField(Ingredient, related_name="ingredients")

    class Meta:
        ordering = ["name"]
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name
