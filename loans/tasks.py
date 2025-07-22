import pandas as pd
from celery import shared_task
from customers.models import Customer
from .models import Loan

@shared_task
def injest_loan_data(file_path):
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        try:
            customer = Customer.objects.get(customer_id=row["Customer ID"])
        except Customer.DoesNotExist:
            continue

        Loan.objects.update_or_create(
            loan_id=row["Loan ID"],
            defaults={
                "customer": customer,
                "loan_amount": row["Loan Amount"],
                "tenure": row["Tenure"],
                "interest_rate": row["Interest Rate"],
                "monthly_installment": row["Monthly payment"],
                "emi_paid_on_time": row["EMIs paid on Time"],
                "start_date": pd.to_datetime(row["Date of Approval"]).date(),
                "end_date": pd.to_datetime(row["End Date"]).date()
            }   
        )
        

