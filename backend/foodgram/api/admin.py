from django.contrib import admin
from .models import (Recipe, Ingredient, IngredientAmount,
                     Tag, Favorite, ShoppingList)

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientAmount)
admin.site.register(Tag)
admin.site.register(Favorite)
admin.site.register(ShoppingList)
