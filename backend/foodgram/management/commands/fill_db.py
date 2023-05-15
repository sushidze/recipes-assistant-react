from django.core.management.base import BaseCommand
from foodgram import models


class Command(BaseCommand):
    def handle(self, **options):
        with open("ingredients.csv") as f:
            for line in f:
                ing = line.split(',')
                models.Ingredient.objects.get_or_create(
                    name=ing[0],
                    measurement_unit=ing[1]
                )
