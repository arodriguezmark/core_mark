from django.db import models

from users.models import User


# Create your models here.

class Item(models.Model):
    price = models.FloatField(null=True, blank=True, default=0)
    branch_id = models.IntegerField(null=True, blank=True)
    instruction = models.CharField(max_length=256, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True, default=0)
    item_variation_total = models.IntegerField(null=True, blank=True)
    item_extra_total = models.IntegerField(null=True, blank=True)

    # def total_price_item(self):
    #     if self.quantity != 0 and self.price != 0:
    #         return self.quantity * self.price
    #
    # def save(self, *args, **kwargs):
    #     self.subtotal = self.total_price_item()
    #     self.total_price = self.subtotal
    #     super(Item, self).save(*args, **kwargs)


class ShoppingCart(models.Model):
    branch_id = models.CharField(max_length=256, null=True, blank=True)
    subtotal = models.FloatField(null=True, blank=True)
    token = models.TextField(null=True, blank=True)
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    discount = models.FloatField(null=True, blank=True)
    delivery_charge = models.IntegerField(null=True, blank=True)
    delivery_time = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True, default=0)
    order_type = models.IntegerField(null=True, blank=True)
    is_advance_order = models.BooleanField(default=False, null=True)
    source = models.IntegerField(null=True, blank=True)
    address_id = models.IntegerField(null=True, blank=True)
    coupon_id = models.IntegerField(null=True, blank=True)
    items = models.ManyToManyField(Item)
