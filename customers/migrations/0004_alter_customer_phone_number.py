# Generated by Django 4.2.23 on 2025-07-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_current_debt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.BigIntegerField(unique=True),
        ),
    ]
