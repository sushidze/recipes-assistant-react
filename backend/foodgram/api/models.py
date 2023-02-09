from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings


class Ingredient(models.Model):
    name = models.CharField(
        max_length=100,
    )
    measurement_unit = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


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


class Recipe(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Recipe author',
        related_name='recipes',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Recipe title',
    )
    text = models.TextField(
        verbose_name='Description',
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(
            1,
            message='Cooking time should be more than 0',
        )]
    )
    tag = models.ManyToManyField(
        Tag,
        related_name='recipes',
    )
    ingredient = models.ManyToManyField(
        Ingredient,
        through='IngredientAmount',
        verbose_name='Composition of the dish',
        related_name='recipes',
    )
    image = models.ImageField(
        verbose_name='Dish image',
        upload_to='recipes/',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )
    amount = models.PositiveIntegerField(
        validators=[MinValueValidator(
            1,
            message='Ingredients amount should be more than 0',
        )]
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=('ingredient', 'recipe'),
            name='unique ingredients amount in one recipe',
        )]


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favorite_users',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite_recipes',
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=('user', 'recipe'),
            name='unique favorite recipe',
        )]


class ShoppingList(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lists',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='lists',
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=('user', 'recipe'),
            name='unique recipe in shopping list'
        )]
