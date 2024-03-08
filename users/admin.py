from cities_light.models import Country
from django import forms
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.urls import path

from users.models import User, Address


# Register your models here.

@admin.register(User)
class ModelNameAdmin(admin.ModelAdmin):
    pass


# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['country'].queryset = Country.objects.filter(name='Venezuela')


# class AddressAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(Address, AddressAdmin)
