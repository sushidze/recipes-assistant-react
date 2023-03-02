from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
    )
    color = models.CharField(
        max_length=7,
        default='#0000FF',
        unique=True,
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=200
    )
    measurement_unit = models.CharField(
        max_length=200
    )

    def __str__(self):
        return f"{self.name}, {self.measurement_unit}"


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipes",
    )
    tags = models.ManyToManyField(
        Tag, through="TagsInRecipe", related_name="recipes"
    )
    name = models.CharField(max_length=200)
    text = models.TextField()
    cooking_time = models.PositiveSmallIntegerField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through="IngredientInRecipe",
        related_name="recipes",
        blank=True,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )
    image = models.ImageField()

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.name


class TagsInRecipe(models.Model):

    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField(
        null=True
    )


class Favorite(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name="favorite",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorite",
    )
    when_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-when_added"]
        unique_together = ("user", "recipe")

    def __str__(self):
        return f"{self.user} added {self.recipe}"


class ShoppingCart(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name="shopping_cart",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="shopping_cart",
    )
    when_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-when_added"]
        unique_together = ("user", "recipe")

    def __str__(self):
        return f"{self.user} added {self.recipe}"
