import pandas as pd
from celery import shared_task
from .models import Customer

@shared_task
def injest_customer_data(file_path):
   df = pd.read_excel(file_path)
   for _, row in df.iterrows():
      Customer.objects.update_or_create(
         customer_id=row["Customer ID"],
         defaults={
               "first_name": row["First Name"],
               "last_name": row["Last Name"],
               "age": row["Age"],
               "phone_number": row["Phone Number"],
               "monthly_salary": row["Monthly Salary"],
               "approved_limit": row["Approved Limit"],
         }
      )
