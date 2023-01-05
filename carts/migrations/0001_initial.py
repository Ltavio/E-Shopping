# Generated by Django 4.1.4 on 2023-01-05 13:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("subtotal_price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("frete", models.DecimalField(decimal_places=2, max_digits=8)),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
