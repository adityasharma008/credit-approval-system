from django.db import models

class Customer(models.Model):
   customer_id = models.AutoField(primary_key=True)
   first_name = models.CharField(max_length=100, blank=False)
   last_name = models.CharField(max_length=100, blank=False)
   age = models.PositiveIntegerField()
   phone_number = models.BigIntegerField(unique=True)
   monthly_salary = models.PositiveIntegerField()
   approved_limit = models.PositiveIntegerField()
   current_debt = models.PositiveIntegerField(default=0)