# Generated by Django 4.1.4 on 2023-01-05 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="payment",
        ),
    ]
