# Generated by Django 4.2.4 on 2023-08-14 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_ordered_order_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='ordered',
        ),
    ]
