from rest_framework import viewsets

from .models import (Recipe, Ingredient, Favorite,
                     IngredientAmount, Tag, ShoppingList)
from .serializers import (RecipeSerializer, IngredientSerializer,
                          ShoppingListSerializer, TagSerializer,
                          IngredientAmountSerializer)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
    
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
