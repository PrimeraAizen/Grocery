# Generated by Django 4.2.4 on 2023-08-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_shippingaddress_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
