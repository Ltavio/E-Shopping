# Generated by Django 4.1.4 on 2023-01-06 19:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories_products", "0001_initial"),
        ("sellers", "0002_initial"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderProduct",
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
                ("quantity_product", models.IntegerField(null=True)),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.order",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name_product", models.CharField(max_length=150, null=True)),
                ("description", models.TextField(null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("price", models.FloatField(null=True, verbose_name=2)),
                ("stock", models.IntegerField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("quantity", models.IntegerField(default=1)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="categories_products.category_product",
                    ),
                ),
                (
                    "orders",
                    models.ManyToManyField(
                        related_name="order_products",
                        through="products.OrderProduct",
                        to="orders.order",
                    ),
                ),
                (
                    "sellers",
                    models.ManyToManyField(
                        related_name="products", to="sellers.seller"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="orderproduct",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.product",
            ),
        ),
    ]
