# Generated by Django 4.1.4 on 2023-01-06 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sellers", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="seller",
            name="is_seller",
        ),
    ]
