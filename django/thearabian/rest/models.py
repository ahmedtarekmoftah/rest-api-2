from django.db import models


class country(models.Model):
    name = models.CharField(max_length=255, default="قريبا")
    title = models.CharField(max_length=255, default="قريبا")

    def __str__(self):
        return f"{self.id}. {self.name}"
