from django.utils import timezone
from django.conf import settings
from django.db import models
from .managers import SoftDeleteManager, SoftDeleteManagerRestore


# Create your models here.

class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, default=None)
    is_deleted = models.BooleanField(default=False)
    soft_delete_objects = SoftDeleteManager()
    objects_restore = SoftDeleteManagerRestore()
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class CarBrand(SoftDeleteModel):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    deleted_at = models.DateTimeField('deleted at', blank=True, null=True)


class CarModel(SoftDeleteModel):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', blank=True, null=True, auto_now=True)


class UserCar(SoftDeleteModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    first_reg = models.DateTimeField('first registration', auto_now_add=True)
    odometer = models.IntegerField()
    deleted_at = models.DateTimeField('deleted at', blank=True, null=True, auto_now=True)
