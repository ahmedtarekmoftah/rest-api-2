from django.db import models


class country(models.Model):
    name = model.CharField(max_length=255, default="قريبا")
    title = model.CharField(max_lenght=255, default="قريبا")

    def __str__(self):
        return f"{self.id}. {self.name}"
