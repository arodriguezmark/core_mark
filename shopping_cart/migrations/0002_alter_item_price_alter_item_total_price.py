# Generated by Django 5.0.2 on 2024-03-12 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='total_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
