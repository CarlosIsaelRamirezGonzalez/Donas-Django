# Generated by Django 5.0.6 on 2024-06-18 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingCart', '0006_order_suggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_arrived',
            field=models.DateField(blank=True, null=True),
        ),
    ]
