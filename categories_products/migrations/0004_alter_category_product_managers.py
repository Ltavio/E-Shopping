# Generated by Django 4.1.4 on 2023-01-04 01:34

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("categories_products", "0003_category_product_is_deleted"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="category_product",
            managers=[
                ("undeleted_objects", django.db.models.manager.Manager()),
            ],
        ),
    ]
