# Generated by Django 5.0.6 on 2024-05-24 14:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventory', '0002_alter_donut_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=350)),
                ('quantity', models.PositiveIntegerField()),
                ('donut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='Inventory.donut')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('bill', models.DecimalField(decimal_places=2, max_digits=5)),
                ('donut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart', to='Inventory.donut')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
