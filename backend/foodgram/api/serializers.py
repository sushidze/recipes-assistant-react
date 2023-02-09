from rest_framework import serializers

from .models import (Recipe, Ingredient, IngredientAmount,
                     Tag, Favorite, ShoppingList)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class IngredientAmountSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit'
    )

    class Meta:
        model = IngredientAmount
        fields = ('id', 'name', 'measurement_unit', 'amount')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('recipe', 'user')


class RecipeSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(many=True, read_only=True)
    ingredient = serializers.StringRelatedField(many=True, read_only=True)
    amount = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('user', 'recipe')
