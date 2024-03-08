from cities_light.models import Country, City, Region
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(primary_key=True, max_length=20, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=256, blank=True, null=True)
    last_name = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "phone_number"

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True,
                              limit_choices_to={'country_id': models.OuterRef('country_id')})
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True,
                             limit_choices_to={'region_id': models.OuterRef('region_id')})
    address = models.CharField(max_length=256, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    reference_point = models.CharField(max_length=256, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.state, self.city, self.address

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
