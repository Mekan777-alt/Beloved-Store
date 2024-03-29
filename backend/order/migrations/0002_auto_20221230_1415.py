# Generated by Django 3.2.14 on 2022-12-30 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baskets', '0007_auto_20221223_1431'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='quantity',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.orders')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baskets.basket')),
            ],
        ),
    ]
