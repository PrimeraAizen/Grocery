# Generated by Django 4.2.4 on 2023-08-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_order_order_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_notes',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='order_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
