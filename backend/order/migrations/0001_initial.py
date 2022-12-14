# Generated by Django 3.2.14 on 2022-12-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.TextField()),
                ('address', models.TextField()),
                ('city', models.TextField()),
                ('index', models.PositiveIntegerField(default=0)),
                ('phone_number', models.CharField(max_length=20)),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product_name', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
            options={
                'verbose_name': 'Заказы',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
    ]
