from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name', 'age', 'phone_number', 'monthly_salary')
    search_fields = ('customer_id', 'first_name', 'last_name')
