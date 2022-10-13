from django.db import models

from apps.brand.models import Brand


class CarModel(models.Model):
    name = models.CharField(max_length = 50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Modelo'
        verbose_name_plural='Modelos'

    def __str__(self):
        return self.name