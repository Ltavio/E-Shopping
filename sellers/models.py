from django.db import models
from django_softdelete.models import SoftDeleteModel, SoftDeleteManager

import uuid


class Seller(SoftDeleteModel, models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    company_name = models.CharField(max_length=150, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    undeleted_objects = SoftDeleteManager()

    client = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="seller",
    )
