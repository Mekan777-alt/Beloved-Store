# Generated by Django 3.2.14 on 2023-02-08 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_rename_order_orderitem_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
    ]
