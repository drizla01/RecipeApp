# Generated by Django 4.1 on 2022-08-23 21:35

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="name",
            field=models.CharField(
                max_length=150, verbose_name=django.contrib.auth.models.User
            ),
        ),
    ]