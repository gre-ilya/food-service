# Generated by Django 4.1.5 on 2023-01-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_rename_pictures_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='source',
            field=models.ImageField(upload_to=''),
        ),
    ]