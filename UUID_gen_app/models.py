import uuid
from django.db import models


class GeneratorManager(models.Manager):
    def get_queryset(self):
        Data.objects.create()
        return super().get_queryset()


class Data(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.TimeField(auto_now_add=True)

    objects = models.Manager()  # The default manager.
    gen = GeneratorManager()  # The generator manager.

    class Meta:
        ordering = ["-created_at"]