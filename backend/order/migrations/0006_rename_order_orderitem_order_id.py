# Generated by Django 3.2.14 on 2023-02-08 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20230207_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order',
            new_name='order_id',
        ),
    ]
