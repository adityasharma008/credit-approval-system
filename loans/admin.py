from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'customer_id', 'loan_amount', 'tenure', 'interest_rate', 'end_date')
    search_fields = ('loan_id', 'customer__first_name', 'customer__last_name')
