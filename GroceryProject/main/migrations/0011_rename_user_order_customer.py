# Generated by Django 4.2.4 on 2023-08-14 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_orderitem_ordered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
    ]
