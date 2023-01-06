# Generated by Django 4.1.4 on 2023-01-06 13:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("addresses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="users",
            field=models.ManyToManyField(
                related_name="Addresses", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
