from django.db import models

from apps.model.models import CarModel
from apps.user.models import User


class Car(models.Model):
    plate = models.CharField(max_length = 10)
    mileage = models.PositiveSmallIntegerField(verbose_name = 'kilometraje')
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete = models.CASCADE)

    class Meta:
        verbose_name='Auto'
        verbose_name_plural='Autos'

    def __str__ (self):
        return '%s %s' % (self.plate, self.user)