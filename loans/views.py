from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CheckEligibilitySerializer
from rest_framework import status
from customers.models import Customer
from .models import Loan
from datetime import datetime

def calculate_emi(principal, annual_rate, months):
   r = (annual_rate / 100) / 12
   emi = principal * r * ((1 + r) ** months) / (((1 + r) ** months) - 1)
   return round(emi, 2)


@api_view(['POST'])
def check_eligibility(request):
   serializer = CheckEligibilitySerializer(data=request.data)
   if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   data = serializer.validated_data
   customer_id = data['customer_id']
   loan_amount = data['loan_amount']
   interest_rate = data['interest_rate']
   tenure = data['tenure']

   customer = Customer.objects.get(pk=customer_id)

   current_loans = Loan.objects.filter(customer=customer)
   total_debt = sum(l.loan_amount for l in current_loans)

   # If sum of current loans of customer > approved limit of customer, credit score = 0
   if total_debt > customer.approved_limit:
      return Response({
         "customer_id": customer_id,
         "approval": False,
         "corrected_interest_rate": None,
         "tenure": tenure,
         "monthly_installment": None
      })
   
   # If sum of all current EMIs > 50% of monthly salary, don’t approve any loans
   new_emi = calculate_emi(loan_amount, interest_rate, tenure)
   total_emi = sum(l.monthly_repayment for l in current_loans) + new_emi
   if total_emi > 0.5 * customer.monthly_salary:
      return Response({
         "customer_id": customer_id,
         "approval": False,
         "corrected_interest_rate": None,
         "tenure": tenure,
         "monthly_installment": None
      })
   
   # Credit score calcuation, each condition assumed to have weight of 25
   #  i.  Past Loans paid on time
   # ii.  No of loans taken in past
   # iii. Loan activity in current year
   # iv.  Loan approved volume
   credit_score = 0
   total_loans = current_loans.count()
   if total_loans > 0:
      on_time = sum(l.emi_paid_on_time / l.tenure for l in current_loans) / total_loans
      credit_score += on_time * 25

      credit_score += min(5, total_loans) * 5

      current_year_loans = sum(1 for l in current_loans if l.start_date.year == datetime.now().year)
      credit_score += min(5, current_year_loans) * 5

      loan_volume = sum(l.loan_amount for l in current_loans)  
      credit_score += min(loan_volume / customer.approved_limit, 1) * 25
   else:
      credit_score = 50 #New customer
   
   approval = False
   corrected_interest_rate = interest_rate

   if credit_score > 50:
      approval = True
   elif 30 < credit_score <= 50:
      if interest_rate >= 12:
         approval = True
      else:
         corrected_interest_rate = 12
   elif 10 < credit_score <= 30:
      if interest_rate >= 16:
         approval = True
      else:
         corrected_interest_rate = 16
   else:
      approval = False

   final_emi = calculate_emi(loan_amount, corrected_interest_rate, tenure)

   return Response({
      "customer_id": customer_id,
      "approval": approval,
      "interest_rate": interest_rate,
      "corrected_interest_rate": corrected_interest_rate,
      "tenure": tenure,
      "monthly_installment": final_emi
   })
