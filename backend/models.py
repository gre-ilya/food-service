from django.db import models


class Picture(models.Model):
    source = models.ImageField(upload_to="")


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    picture_id = models.ForeignKey(Picture, related_name='ingredient_picture', on_delete=models.DO_NOTHING)


class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    picture_id = models.ForeignKey(Picture, default='matrix1.png', related_name='user_picture', on_delete=models.DO_NOTHING)
    stars = models.IntegerField(default=0)
    city = models.CharField(max_length=200, default='null')
    role = models.CharField(max_length=200, default='user')


class Dish(models.Model):
    name = models.CharField(max_length=200)
    picture_id = models.ForeignKey(Picture, related_name='dish_picture', on_delete=models.DO_NOTHING)
    difficulty = models.IntegerField()
    description = models.TextField(max_length=200)
    author_id = models.ForeignKey(User, related_name='dish_author', on_delete=models.CASCADE)
    cooktime = models.IntegerField()


class IngredientsDishes(models.Model):
    ingredient_id = models.ForeignKey(Ingredient, related_name='ingredient', on_delete=models.DO_NOTHING)
    dish_id = models.ForeignKey(Dish, related_name='dish', on_delete=models.CASCADE)


class RecipeStep(models.Model):
    dish_id = models.ForeignKey(Dish, related_name='recipe_dish', on_delete=models.CASCADE)
    picture_id = models.ForeignKey(Picture, related_name='recipe_picture', on_delete=models.DO_NOTHING)
    step_desc = models.TextField()
