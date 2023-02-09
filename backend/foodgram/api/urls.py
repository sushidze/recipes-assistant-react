from rest_framework.routers import SimpleRouter

from django.urls import include, path
from .views import RecipeViewSet, TagViewSet, IngredientViewSet

router = SimpleRouter()
router.register('recipes', RecipeViewSet)
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]