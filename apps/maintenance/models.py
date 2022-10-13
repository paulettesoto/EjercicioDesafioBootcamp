from django.db import models

from apps.car.models import Car

class Maintenance(models.Model):
    mileage = models.PositiveSmallIntegerField(verbose_name = 'kilometraje')
    description = models.CharField(max_length = 200)
    price = models.PositiveSmallIntegerField(verbose_name = 'costo')
    date = models.DateField(verbose_name='Fecha ')
    car = models.OneToOneField(Car, on_delete = models.CASCADE)

    class Meta:
        verbose_name='Mantenimiento'
        verbose_name_plural='Mantenimientos'

    def __str__ (self):
        return '%s %s %s' % (self.car, self.price, self.date)