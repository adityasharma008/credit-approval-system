# Generated by Django 4.2.23 on 2025-07-21 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('tenure', models.PositiveIntegerField()),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('monthly_repayment', models.DecimalField(decimal_places=2, max_digits=12)),
                ('emi_paid_on_time', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='customers.customer')),
            ],
        ),
    ]
