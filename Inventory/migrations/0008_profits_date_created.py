# Generated by Django 5.0.6 on 2024-06-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0007_profits'),
    ]

    operations = [
        migrations.AddField(
            model_name='profits',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
