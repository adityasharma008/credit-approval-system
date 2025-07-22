from rest_framework import serializers
from customers.models import Customer
from .models import Loan

class CheckEligibilitySerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    loan_amount = serializers.FloatField()
    interest_rate = serializers.FloatField()
    tenure = serializers.IntegerField()

    def validate_customer_id(self, value):
        if not Customer.objects.filter(customer_id=value).exists():
            raise serializers.ValidationError("Customer with this ID does not exist")
        return value

    def validate_loan_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Loan amount must be positive")
        return value
    
    def validate_interest_rate(self, value):
        if value < 0:
            raise serializers.ValidationError("Interest rate must be positive")
        return value

    def validate_tenure(self, value):
        if value <= 0:
            raise serializers.ValidationError("Tenure must be positive")
        return value
    
class ViewLoanSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(source='customer.customer_id')
    customer_first_name = serializers.CharField(source='customer.first_name')
    customer_last_name = serializers.CharField(source='customer.last_name')
    customer_phone_number = serializers.CharField(source='customer.phone_number')
    customer_age = serializers.IntegerField(source='customer.age')

    class Meta:
        model = Loan
        fields = [
            'loan_id',
            'customer_id',
            'customer_first_name',
            'customer_last_name',
            'customer_phone_number',
            'customer_age',
            'loan_amount',
            'interest_rate',
            'monthly_installment',
            'tenure'
        ]
