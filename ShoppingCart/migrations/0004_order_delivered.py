# Generated by Django 5.0.6 on 2024-05-27 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingCart', '0003_shoppingcart_suggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
