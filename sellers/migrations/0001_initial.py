# Generated by Django 4.1 on 2023-01-11 21:56

from django.db import migrations, models
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Seller",
            fields=[
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("company_name", models.CharField(max_length=150, unique=True)),
                ("cnpj", models.CharField(max_length=14, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("undeleted_objects", django.db.models.manager.Manager()),
            ],
        ),
    ]
