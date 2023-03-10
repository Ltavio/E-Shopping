from django.db import models
import uuid

# Create your models here.


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name_product = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    price = models.FloatField(2, null=True)
    stock = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    # quantity = models.IntegerField(null=True, blank=True,)

    seller = models.ForeignKey(
        "sellers.Seller",
        on_delete=models.CASCADE,
        related_name="products",
    )

    category = models.ForeignKey(
        "categories_products.Category_product",
        on_delete=models.CASCADE,
        related_name="products",
    )

    orders = models.ManyToManyField(
        "orders.Order",
        through="products.OrderProduct",
        related_name="products",
    )


class OrderProduct(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    quantity_product = models.IntegerField(null=True)
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="order_products",
    )
    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="order_products",
    )
