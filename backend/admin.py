from django.contrib import admin
from .models import Picture, Ingredient, Dish, IngredientsDishes, User, RecipeStep

admin.site.register(Picture)
admin.site.register(Ingredient)
admin.site.register(Dish)
admin.site.register(IngredientsDishes)
admin.site.register(User)
admin.site.register(RecipeStep)
# Register your models here.
