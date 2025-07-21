from django.db import models
from customers.models import Customer

class Loan(models.Model):
   loan_id = models.AutoField(primary_key=True)
   customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="loans")
   loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
   tenure = models.PositiveIntegerField()
   interest_rate = models.DecimalField(max_digits=4, decimal_places=2)
   monthly_repayment = models.DecimalField(max_digits=12, decimal_places=2)
   emi_paid_on_time = models.PositiveIntegerField(default=0)
   start_date = models.DateField()
   end_date = models.DateField()