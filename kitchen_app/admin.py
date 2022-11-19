from django.contrib import admin

from kitchen_app.models import (Cook, Ingredient, Dish, DishType)

admin.site.register(Cook)
admin.site.register(Ingredient)
admin.site.register(DishType)
admin.site.register(Dish)
