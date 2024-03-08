from django.db import models

from users.models import User


# Create your models here.
class Item(models.Model):
    item_id = models.IntegerField(null=True, blank=True)
    item_price = models.FloatField(null=True, blank=True)
    branch_id = models.IntegerField(null=True, blank=True)
    instruction = models.CharField(max_length=256, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    item_variation_total = models.IntegerField(null=True, blank=True)
    item_extra_total = models.IntegerField(null=True, blank=True)


class ShoppingCart(models.Model):
    branch_id = models.IntegerField(null=True, blank=True)
    subtotal = models.FloatField(null=True, blank=True)
    token = models.TextField(null=True, blank=True)
    customer_id = models.OneToOneField(User, on_delete=models.CASCADE)
    discount = models.FloatField(null=True, blank=True)
    delivery_charge = models.FloatField(null=True, blank=True)
    delivery_time = models.FloatField(null=True, blank=True)
    total = models.CharField(max_length=256, null=True, blank=True)
    order_type = models.IntegerField(null=True, blank=True)
    is_advance_order = models.IntegerField(null=True, blank=True)
    source = models.IntegerField(null=True, blank=True)
    address_id = models.IntegerField(null=True, blank=True)
    coupon_id = models.IntegerField(null=True, blank=True)
    items = models.ManyToManyField(Item)
