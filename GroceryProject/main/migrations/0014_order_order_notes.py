# Generated by Django 4.2.4 on 2023-08-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]