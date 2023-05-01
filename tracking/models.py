from django.db import models

from base.mixins.model_mixin import PrimaryKeyMixin


class Tracking(PrimaryKeyMixin):
    method = models.CharField(max_length=16)
    url = models.CharField(max_length=255)
    data = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.method} | {self.url} | {self.data['message']}"
